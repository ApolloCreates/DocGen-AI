from pydantic import BaseModel, Field

from app.parser.models import ParsedFile


class RepositoryIndex(BaseModel):

    files: list[ParsedFile] = Field(default_factory=list)

    total_files: int = 0
    total_classes: int = 0
    total_functions: int = 0
    total_imports: int = 0
    total_endpoints: int = 0

    frameworks: list[str] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)

    file_tree: list[str] = Field(default_factory=list)
    
    dependencies: list[str] = Field(default_factory=list)

    entry_points: list[str] = Field(default_factory=list)

    config_files: list[str] = Field(default_factory=list)

    package_manager: str | None = None