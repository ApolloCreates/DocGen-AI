from pathlib import Path

from tree_sitter_language_pack import get_parser

from app.parser.language import LanguageDetector


class ASTParser:

    def __init__(self):

        self.detector = LanguageDetector()

    def parse(self, path: Path):

        language = self.detector.detect(path)

        if language is None:
            return None

        parser = get_parser(language)

        source = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        tree = parser.parse(
            source.encode("utf-8")
        )

        return tree, source, language