from pathlib import Path

from app.github.ignore import IGNORE_DIRS, IGNORE_FILES
from app.github.models import SourceFile


class RepositoryScanner:

    def scan(self, root: Path) -> list[SourceFile]:

        files: list[SourceFile] = []

        for path in root.rglob("*"):

            if not path.is_file():
                continue

            if any(part in IGNORE_DIRS for part in path.parts):
                continue

            if path.name in IGNORE_FILES:
                continue

            files.append(
                SourceFile(
                    path=str(path.relative_to(root)),
                    extension=path.suffix,
                    size=path.stat().st_size,
                )
            )

        return files