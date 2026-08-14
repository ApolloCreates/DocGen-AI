from pydantic import BaseModel, Field


class ModuleContext(BaseModel):
    path: str

    classes: list[str] = Field(default_factory=list)

    functions: list[str] = Field(default_factory=list)

    imports: list[str] = Field(default_factory=list)


class ReadmeContext(BaseModel):

    project_name: str

    languages: list[str]

    total_files: int

    total_classes: int

    total_functions: int

    modules: list[ModuleContext] = Field(default_factory=list)