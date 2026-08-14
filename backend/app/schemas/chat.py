from pydantic import BaseModel


class RepositoryChatRequest(BaseModel):
    repository: str
    question: str


class RepositoryChatResponse(BaseModel):
    answer: str