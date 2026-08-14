from app.agents.base import BaseAgent
from app.prompts.summary import SUMMARY_PROMPT

from app.knowledge.formatter import (
    KnowledgeFormatter,
)

class SummaryAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.formatter = (
            KnowledgeFormatter()
        )

    def generate_summary(
        self,
        knowledge,
    ):

        context = self.formatter.format(
            knowledge
        )

        prompt = SUMMARY_PROMPT.format(
            context=context
        )

        return self.generate_content(prompt)