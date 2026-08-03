from app.github.clone import RepositoryCloner
from app.github.models import Repository
from app.github.scanner import RepositoryScanner
from app.parser.service import ParserService


class RepositoryService:

    def __init__(self):

        self.cloner = RepositoryCloner()

        self.scanner = RepositoryScanner()

        self.parser = ParserService()

    def analyze(self, url: str) -> Repository:

        repo_path = self.cloner.clone(url)

        files = self.scanner.scan(repo_path)

        parsed_files = []

        for file in files:

            parsed = self.parser.analyze(
                repo_path / file.path
            )

            if parsed is not None:
                parsed_files.append(parsed)

        return Repository(
            name=repo_path.name,
            root=repo_path,
            files=files,
            parsed_files=parsed_files,
        )