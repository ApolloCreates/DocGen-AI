from app.github.scanner import RepositoryScanner

from app.pipeline.base import PipelineStage


class ScanStage(PipelineStage):

    def __init__(self):

        self.scanner = RepositoryScanner()

    def run(self, repository):

        repository.files = self.scanner.scan(
            repository.root
        )

        return repository