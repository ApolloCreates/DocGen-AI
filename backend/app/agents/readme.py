from google import genai

from app.context.builder import ContextBuilder
from app.core.settings import get_settings
from app.prompts.readme import README_PROMPT


class ReadmeAgent:

    def __init__(self):

        settings = get_settings()

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.context = ContextBuilder()

    def generate(self, repository):

        context = self.context.build_readme(repository)

        prompt = README_PROMPT.format(
            context=context.model_dump_json(indent=2)
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text