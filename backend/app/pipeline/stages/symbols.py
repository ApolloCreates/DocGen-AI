from app.indexer.builder import SymbolBuilder

from app.pipeline.base import PipelineStage


class SymbolStage(PipelineStage):

    def __init__(self):

        self.builder = SymbolBuilder()

    def run(self, repository):

        repository.symbols = self.builder.build(
            repository
        )

        return repository