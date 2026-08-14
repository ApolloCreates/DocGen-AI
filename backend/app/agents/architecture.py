from app.agents.base import BaseAgent
from app.prompts.architecture import (
    ARCHITECTURE_PROMPT,
)

from app.knowledge.formatter import (
    KnowledgeFormatter,
)

class ArchitectureAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.formatter = (
            KnowledgeFormatter()
        )

    def generate_architecture(
        self,
        knowledge,
    ):

        context = self.formatter.format(
            knowledge
        )

        prompt = ARCHITECTURE_PROMPT.format(
            context=context
        )

        return self.generate_content(prompt)