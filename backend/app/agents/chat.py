from app.agents.base import BaseAgent
from app.knowledge.formatter import KnowledgeFormatter


CHAT_PROMPT = """
You are an AI assistant that explains software repositories.

Answer the user's question using ONLY the repository information
provided below.

Rules:
- Do not invent files, classes, functions, dependencies, or behavior.
- If the repository information does not contain enough information,
  clearly say that you cannot determine it.
- Be concise but useful.
- When relevant, mention specific files, classes, or functions.
- Explain technical concepts in simple language.

Repository information:

{context}

User question:

{question}

Answer:
"""


class ChatAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.formatter = KnowledgeFormatter()

    def answer(self, knowledge, question: str):

        context = self.formatter.format(
            knowledge
        )

        prompt = CHAT_PROMPT.format(
            context=context,
            question=question,
        )

        return self.generate_content(prompt).strip()