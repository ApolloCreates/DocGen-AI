from pydantic import BaseModel, Field


class Module(BaseModel):
    path: str
    imports: list[str] = Field(default_factory=list)
    classes: list[str] = Field(default_factory=list)
    functions: list[str] = Field(default_factory=list)


class RepositoryMap(BaseModel):
    modules: list[Module] = Field(default_factory=list)