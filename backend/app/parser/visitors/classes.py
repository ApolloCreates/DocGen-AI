from app.parser.models import ClassSymbol

from .base import BaseVisitor


class ClassVisitor(BaseVisitor):

    def visit(
        self,
        node,
        source,
        result,
    ):

        if node.type != "class_definition":
            return

        name = node.child_by_field_name("name")

        if name is None:
            return

        result.classes.append(

            ClassSymbol(
                name=source[
                    name.start_byte:name.end_byte
                ],
                line=node.start_point[0] + 1,
            )
        )