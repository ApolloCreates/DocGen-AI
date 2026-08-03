from app.indexer.builder import RepositoryIndexer

from app.pipeline.base import PipelineStage


class IndexStage(PipelineStage):

    def __init__(self):

        self.indexer = RepositoryIndexer()

    def run(self, repository):

        repository.index = self.indexer.build(
            repository
        )

        return repository