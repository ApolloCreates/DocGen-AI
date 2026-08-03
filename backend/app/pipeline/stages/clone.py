from app.github.clone import RepositoryCloner

from app.pipeline.base import PipelineStage


class CloneStage(PipelineStage):

    def __init__(self):

        self.cloner = RepositoryCloner()

    def run(self, repository):

        path = self.cloner.clone(repository.url)

        repository.root = path

        repository.name = path.name

        return repository