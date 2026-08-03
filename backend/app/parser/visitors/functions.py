from app.parser.models import FunctionSymbol

from .base import BaseVisitor


class FunctionVisitor(BaseVisitor):

    def visit(
        self,
        node,
        source,
        result,
    ):

        if node.type != "function_definition":
            return

        name = node.child_by_field_name("name")

        if name is None:
            return

        result.functions.append(

            FunctionSymbol(
                name=source[
                    name.start_byte:name.end_byte
                ],
                line=node.start_point[0] + 1,
            )
        )