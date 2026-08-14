from groq import Groq

from app.core.settings import get_settings


class BaseAgent:

    def __init__(self):

        settings = get_settings()

        if not settings.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is not configured"
            )

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = "llama-3.3-70b-versatile"

    def generate_content(
        self,
        prompt: str,
    ):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
            response_format={
                "type": "json_object"
            },
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError(
                "LLM returned an empty response"
            )

        return content