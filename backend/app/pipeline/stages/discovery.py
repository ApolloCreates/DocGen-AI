from app.discovery.builder import DiscoveryBuilder
from app.pipeline.base import PipelineStage


class DiscoveryStage(PipelineStage):

    def __init__(self):

        self.builder = DiscoveryBuilder()

    def run(self, repository):

        repository.discovery = self.builder.build(
            repository
        )

        return repository