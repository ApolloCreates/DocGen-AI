import json

from app.agents.base import BaseAgent
from app.knowledge.formatter import KnowledgeFormatter
from app.prompts.documentation import DOCUMENTATION_PROMPT
from app.utils.mermaid import sanitize_mermaid


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

        print(
            "\n========== DOCUMENTATION MODEL RESPONSE =========="
        )
        print(response)
        print(
            "===================================================\n"
        )

        return self._parse_response(response)

    def _parse_response(self, response):

        response = response.strip()

        if response.startswith("```"):

            lines = response.splitlines()

            if lines and lines[0].startswith("```"):
                lines = lines[1:]

            if (
                lines
                and lines[-1].strip() == "```"
            ):
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

        missing = required - set(result.keys())

        if missing:

            raise ValueError(
                f"Documentation agent missing fields: {missing}"
            )

        extra = set(result.keys()) - required

        if extra:

            raise ValueError(
                f"Documentation agent returned unexpected fields: {extra}"
            )

        # Clean common Mermaid syntax mistakes
        # produced by the LLM.
        result["architecture"] = sanitize_mermaid(
            result["architecture"]
        )

        return {
            "readme": result["readme"],
            "architecture": result["architecture"],
            "summary": result["summary"],
            "installation": result["installation"],
        }