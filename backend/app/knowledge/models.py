from pydantic import BaseModel, Field


class ModuleKnowledge(BaseModel):

    path: str

    language: str

    imports: list[str] = Field(default_factory=list)

    classes: list[str] = Field(default_factory=list)

    functions: list[str] = Field(default_factory=list)


class RepositoryStatistics(BaseModel):

    total_files: int

    total_classes: int

    total_functions: int


class RepositoryKnowledge(BaseModel):

    project_name: str

    languages: list[str] = Field(default_factory=list)

    frameworks: list[str] = Field(default_factory=list)

    dependencies: list[str] = Field(default_factory=list)

    entry_points: list[str] = Field(default_factory=list)

    config_files: list[str] = Field(default_factory=list)

    package_manager: str | None = None

    tree: str = ""

    statistics: RepositoryStatistics

    modules: list[ModuleKnowledge] = Field(
        default_factory=list
    )