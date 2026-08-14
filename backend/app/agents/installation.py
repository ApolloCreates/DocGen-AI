from app.agents.base import BaseAgent
from app.prompts.installation import (
    INSTALLATION_PROMPT,
)

from app.knowledge.formatter import (
    KnowledgeFormatter,
)

class InstallationAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.formatter = (
            KnowledgeFormatter()
        )

    def generate_installation(
        self,
        knowledge,
    ):

        context = self.formatter.format(
            knowledge
        )

        prompt = INSTALLATION_PROMPT.format(
            context=context
        )

        return self.generate_content(prompt)