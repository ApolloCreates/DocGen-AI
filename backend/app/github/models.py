from pathlib import Path
from pydantic import BaseModel, Field

from app.parser.models import ParsedFile


class SourceFile(BaseModel):
    path: str
    extension: str
    size: int


class Repository(BaseModel):
    name: str
    root: Path

    files: list[SourceFile] = Field(default_factory=list)

    parsed_files: list[ParsedFile] = Field(default_factory=list)