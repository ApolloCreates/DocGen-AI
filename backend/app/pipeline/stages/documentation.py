from app.agents.readme import ReadmeAgent

from app.pipeline.base import PipelineStage


class DocumentationStage(PipelineStage):

    def __init__(self):

        self.agent = ReadmeAgent()

    def run(self, repository):

        repository.documentation[
            "README.md"
        ] = self.agent.generate(
            repository
        )

        return repository