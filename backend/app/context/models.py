from pydantic import BaseModel


class ReadmeContext(BaseModel):
    project_name: str

    frameworks: list[str]

    languages: list[str]

    total_files: int

    total_classes: int

    total_functions: int

    total_endpoints: int

    dependencies: list[str]

    package_manager: str | None

    entry_points: list[str]

    file_tree: list[str]

    sample_classes: list[str]

    sample_functions: list[str]