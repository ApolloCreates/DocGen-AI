from google import genai

from app.context.builder import ContextBuilder
from app.prompts.readme import README_PROMPT


class ReadmeAgent:

    def __init__(self):

        self.client = genai.Client()

        self.context = ContextBuilder()

    def generate(self, repository):

        context = self.context.build_readme(
            repository
        )

        prompt = README_PROMPT.format(

            context=context.model_dump_json(
                indent=2
            )

        )

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

        )

        return response.text