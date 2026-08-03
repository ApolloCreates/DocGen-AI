from app.parser.models import ParsedFile

from app.parser.visitors.classes import (
    ClassVisitor,
)

from app.parser.visitors.functions import (
    FunctionVisitor,
)

from app.parser.visitors.imports import (
    ImportVisitor,
)
from app.parser.visitors.endpoints import EndpointVisitor


class PythonPlugin:

    def __init__(self):

        self.visitors = [

            ImportVisitor(),

            ClassVisitor(),

            FunctionVisitor(),

            EndpointVisitor(),

        ]

    def extract(
        self,
        tree,
        source,
        path,
    ):

        result = ParsedFile(
            path=path,
            language="python",
        )

        stack = [tree.root_node]

        while stack:

            node = stack.pop()

            for visitor in self.visitors:

                visitor.visit(
                    node,
                    source,
                    result,
                )

            stack.extend(node.children)

        return result