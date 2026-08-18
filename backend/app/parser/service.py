from app.parser.plugins.python import PythonPlugin
from app.parser.plugins.javascript import JavaScriptPlugin

from app.parser.parser import ASTParser


class ParserService:

    def __init__(self):

        self.parser = ASTParser()

        self.plugins = {
            "python": PythonPlugin(),
            "javascript": JavaScriptPlugin(),
            "typescript": JavaScriptPlugin(),
            "tsx": JavaScriptPlugin(),
        }

    def analyze(self, path):

        parsed = self.parser.parse(path)

        if parsed is None:
            return None

        tree, source, language = parsed

        plugin = self.plugins.get(language)

        if plugin is None:
            return None

        if language == "python":

            return plugin.extract(
                tree,
                source,
                str(path),
            )

        return plugin.extract(
            tree,
            source,
            str(path),
            language=language,
        )