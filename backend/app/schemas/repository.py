from pydantic import BaseModel, HttpUrl


class RepositoryAnalyzeRequest(BaseModel):
    url: HttpUrl