from app.parser.plugins.python import PythonPlugin
from app.parser.parser import ASTParser


class ParserService:

    def __init__(self):

        self.parser = ASTParser()

        self.plugins = {

            "python": PythonPlugin(),

        }

    def analyze(self, path):

        parsed = self.parser.parse(path)

        if parsed is None:
            return None

        tree, source, language = parsed

        plugin = self.plugins.get(language)

        if plugin is None:
            return None

        return plugin.extract(

            tree,

            source,

            str(path),
        )