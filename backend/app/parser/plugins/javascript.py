from app.parser.models import (
    ParsedFile,
    ImportSymbol,
    ClassSymbol,
    FunctionSymbol,
    EndpointSymbol,
)


class JavaScriptPlugin:

    def extract(
        self,
        tree,
        source,
        path,
        language="javascript",
    ):

        result = ParsedFile(
            path=path,
            language=language,
        )

        def walk(node):

            node_type = node.type

            # -----------------------------------------
            # Imports
            # -----------------------------------------

            if node_type == "import_statement":

                text = source[
                    node.start_byte:node.end_byte
                ].decode("utf-8") if isinstance(
                    source, bytes
                ) else source[
                    node.start_byte:node.end_byte
                ]

                result.imports.append(
                    ImportSymbol(
                        module=text.strip()
                    )
                )

            # -----------------------------------------
            # Classes
            # -----------------------------------------

            elif node_type == "class_declaration":

                name_node = node.child_by_field_name(
                    "name"
                )

                if name_node:

                    name = source[
                        name_node.start_byte:
                        name_node.end_byte
                    ]

                    result.classes.append(
                        ClassSymbol(
                            name=name,
                            line=name_node.start_point.row + 1,
                        )
                    )

            # -----------------------------------------
            # Functions
            # -----------------------------------------

            elif node_type in {
                "function_declaration",
                "function",
                "arrow_function",
                "method_definition",
            }:

                name_node = node.child_by_field_name(
                    "name"
                )

                if name_node:

                    name = source[
                        name_node.start_byte:
                        name_node.end_byte
                    ]

                else:

                    name = node_type

                result.functions.append(
                    FunctionSymbol(
                        name=name,
                        line=node.start_point.row + 1,
                    )
                )

            # -----------------------------------------
            # Express Routes
            # -----------------------------------------

            if node_type == "call_expression":

                function_node = (
                    node.child_by_field_name(
                        "function"
                    )
                )

                arguments_node = (
                    node.child_by_field_name(
                        "arguments"
                    )
                )

                if function_node and arguments_node:

                    function_text = source[
                        function_node.start_byte:
                        function_node.end_byte
                    ]

                    if function_text in {
                        "app.get",
                        "app.post",
                        "app.put",
                        "app.patch",
                        "app.delete",
                        "router.get",
                        "router.post",
                        "router.put",
                        "router.patch",
                        "router.delete",
                    }:

                        children = arguments_node.named_children

                        if children:

                            first = children[0]

                            path_text = source[
                                first.start_byte:
                                first.end_byte
                            ]

                            method = (
                                function_text
                                .split(".")[-1]
                                .upper()
                            )

                            result.endpoints.append(
                                EndpointSymbol(
                                    method=method,
                                    path=path_text,
                                    function=function_text,
                                    line=node.start_point.row + 1,
                                )
                            )

            for child in node.children:
                walk(child)

        walk(tree.root_node)

        return result