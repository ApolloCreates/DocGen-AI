from pydantic import BaseModel, Field


class DiscoveryResult(BaseModel):

    frameworks: list[str] = Field(default_factory=list)

    dependencies: list[str] = Field(default_factory=list)

    entry_points: list[str] = Field(default_factory=list)

    config_files: list[str] = Field(default_factory=list)

    package_manager: str | None = None