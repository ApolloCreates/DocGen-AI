from app.parser.models import FunctionSymbol


class FunctionVisitor:

    def visit(self, node, source, result):

        if node.type != "function_definition":
            return

        name_node = node.child_by_field_name("name")

        if name_node is None:
            return

        source_bytes = source.encode("utf-8")

        name = source_bytes[
            name_node.start_byte:
            name_node.end_byte
        ].decode("utf-8")

        result.functions.append(
            FunctionSymbol(
                name=name,
                line=node.start_point[0] + 1,
            )
        )