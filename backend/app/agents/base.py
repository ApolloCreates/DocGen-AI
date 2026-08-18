from click import prompt
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

        self.model = "openai/gpt-oss-120b"

    def generate_content(
        self,
        prompt: str,
        json_mode: bool = False,
    ):

        kwargs = {
            "model": "openai/gpt-oss-120b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        if json_mode:
            kwargs["response_format"] = {
                "type": "json_object"
            }

        response = self.client.chat.completions.create(
            **kwargs
        )

        return response.choices[0].message.content