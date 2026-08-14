import json

from app.agents.base import BaseAgent
from app.knowledge.formatter import KnowledgeFormatter
from app.prompts.documentation import DOCUMENTATION_PROMPT


class DocumentationAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.formatter = KnowledgeFormatter()

    def generate(self, knowledge):

        context = self.formatter.format(
            knowledge
        )

        prompt = DOCUMENTATION_PROMPT.format(
            context=context
        )

        response = self.generate_content(
            prompt,
            json_mode=True,
        )

        return self._parse_response(response)

    def _parse_response(self, response):

        response = response.strip()

        if response.startswith("```"):

            lines = response.splitlines()

            if lines and lines[0].startswith("```"):
                lines = lines[1:]

            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]

            response = "\n".join(lines)

        try:

            result = json.loads(response)

        except json.JSONDecodeError as exc:

            raise ValueError(
                "Documentation agent returned invalid JSON"
            ) from exc

        required = {
            "readme",
            "architecture",
            "summary",
            "installation",
        }

        if set(result.keys()) != required:

            raise ValueError(
                "Documentation agent returned unexpected fields"
            )

        return result