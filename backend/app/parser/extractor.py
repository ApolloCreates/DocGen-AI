from app.parser.models import *


class ASTExtractor:

    def extract(
        self,
        root,
        source,
    ):

        imports = []

        classes = []

        functions = []

        stack = [root]

        while stack:

            node = stack.pop()

            if node.type == "class_definition":

                name = node.child_by_field_name("name")

                classes.append(
                    Class(
                        name=source[
                            name.start_byte:name.end_byte
                        ],
                        line=node.start_point[0] + 1,
                    )
                )

            elif node.type == "function_definition":

                name = node.child_by_field_name("name")

                functions.append(
                    Function(
                        name=source[
                            name.start_byte:name.end_byte
                        ],
                        line=node.start_point[0] + 1,
                    )
                )

            elif node.type in (
                "import_statement",
                "import_from_statement",
            ):

                imports.append(
                    Import(
                        module=source[
                            node.start_byte:node.end_byte
                        ]
                    )
                )

            stack.extend(node.children)

        return imports, classes, functions