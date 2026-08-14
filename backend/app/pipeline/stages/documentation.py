from pathlib import Path

from app.agents.documentation import DocumentationAgent
from app.knowledge.builder import KnowledgeBuilder
from app.pipeline.base import PipelineStage
from app.services.archive import create_documentation_zip


class DocumentationStage(PipelineStage):

    def __init__(self):

        self.builder = KnowledgeBuilder()

        self.agent = DocumentationAgent()

    def run(self, repository):

        knowledge = self.builder.build(
            repository
        )

        generated = self.agent.generate(
            knowledge
        )

        docs = {
            "README.md": generated["readme"],
            "ARCHITECTURE.md": generated["architecture"],
            "SUMMARY.md": generated["summary"],
            "INSTALLATION.md": generated["installation"],
        }

        repository.documentation = docs

        output = Path("outputs") / repository.name

        output.mkdir(
            parents=True,
            exist_ok=True,
        )

        for filename, content in docs.items():

            (output / filename).write_text(
                content,
                encoding="utf-8",
            )

        zip_path = create_documentation_zip(
            output
        )

        repository.metadata[
            "documentation_zip"
        ] = str(zip_path)

        return repository