from pathlib import Path


LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
}


class LanguageDetector:

    def detect(self, path: Path) -> str | None:
        return LANGUAGE_MAP.get(path.suffix)