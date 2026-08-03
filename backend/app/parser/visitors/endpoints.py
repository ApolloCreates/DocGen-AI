from app.parser.models import EndpointSymbol
from app.parser.visitors.base import BaseVisitor


HTTP_METHODS = {
    "get",
    "post",
    "put",
    "delete",
    "patch",
    "options",
    "head",
}


class EndpointVisitor(BaseVisitor):

    def visit(self, node, source, result):

        if node.type != "decorated_definition":
            return

        function_node = None

        decorator_node = None

        for child in node.children:

            if child.type == "decorator":
                decorator_node = child

            elif child.type == "function_definition":
                function_node = child

        if function_node is None or decorator_node is None:
            return

        text = source[
            decorator_node.start_byte:
            decorator_node.end_byte
        ]

        method = None

        for http_method in HTTP_METHODS:

            if f".{http_method}(" in text:

                method = http_method.upper()
                break

        if method is None:
            return

        path = "/"

        first_quote = text.find('"')

        if first_quote == -1:
            first_quote = text.find("'")

        if first_quote != -1:

            quote = text[first_quote]

            second_quote = text.find(
                quote,
                first_quote + 1,
            )

            if second_quote != -1:

                path = text[
                    first_quote + 1:
                    second_quote
                ]

        name = function_node.child_by_field_name("name")

        result.endpoints.append(

            EndpointSymbol(

                method=method,

                path=path,

                function=source[
                    name.start_byte:
                    name.end_byte
                ],

                line=function_node.start_point[0] + 1,
            )
        )