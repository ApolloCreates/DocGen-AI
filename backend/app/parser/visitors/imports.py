from app.parser.models import ImportSymbol

from .base import BaseVisitor


class ImportVisitor(BaseVisitor):

    def visit(
        self,
        node,
        source,
        result,
    ):

        if node.type not in (
            "import_statement",
            "import_from_statement",
        ):
            return

        result.imports.append(

            ImportSymbol(
                module=source[
                    node.start_byte:node.end_byte
                ]
            )
        )