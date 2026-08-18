from app.agents.base import BaseAgent
from app.knowledge.formatter import KnowledgeFormatter
from app.prompts.documentation import DOCUMENTATION_PROMPT
from app.prompts.architecture import ARCHITECTURE_PROMPT
from app.prompts.summary import SUMMARY_PROMPT
from app.prompts.installation import INSTALLATION_PROMPT
from app.prompts.readme import README_PROMPT
from app.utils.mermaid import sanitize_mermaid


class DocumentationAgent(BaseAgent):

    def __init__(self):
        super().__init__()

        self.formatter = KnowledgeFormatter()

    def generate(self, knowledge):

        context = self.formatter.format(
            knowledge
        )

        print(
            "\n========== DOCUMENTATION GENERATION =========="
        )

        readme = self._generate_document(
            README_PROMPT,
            context,
            "README",
        )

        architecture = self._generate_document(
            ARCHITECTURE_PROMPT,
            context,
            "ARCHITECTURE",
        )

        summary = self._generate_document(
            SUMMARY_PROMPT,
            context,
            "SUMMARY",
        )

        installation = self._generate_document(
            INSTALLATION_PROMPT,
            context,
            "INSTALLATION",
        )

        architecture = sanitize_mermaid(
            architecture
        )

        print(
            "========== DOCUMENTATION COMPLETE ==========\n"
        )

        return {
            "readme": readme,
            "architecture": architecture,
            "summary": summary,
            "installation": installation,
        }

    def _generate_document(
        self,
        template,
        context,
        name,
    ):

        prompt = template.format(
            context=context
        )

        print(
            f"Generating {name} documentation..."
        )

        response = self.generate_content(
            prompt,
            json_mode=False,
        )

        return self._clean_markdown(
            response
        )

    def _clean_markdown(self, response):

        response = response.strip()

        # Remove accidental markdown fences
        # around the entire response.

        if response.startswith("```markdown"):

            response = response[
                len("```markdown"):
            :]

        elif response.startswith("```"):

            response = response[
                len("```"):
            ]

        if response.endswith("```"):

            response = response[:-3]

        return response.strip()