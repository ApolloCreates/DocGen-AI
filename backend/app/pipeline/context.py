from pathlib import Path

from pydantic import BaseModel, Field

from app.github.models import SourceFile
from app.parser.models import ParsedFile
from app.indexer.models import RepositoryIndex, RepositoryIndex, RepositorySymbols


class RepositoryContext(BaseModel):
    """
    Shared object passed through every pipeline stage.
    Each stage enriches this object with additional information.
    """

    # Input
    url: str

    # Repository information
    name: str = ""
    root: Path | None = None

    # Scan Stage
    files: list[SourceFile] = Field(default_factory=list)

    # Parse Stage
    parsed_files: list[ParsedFile] = Field(default_factory=list)

    # Graph Stage (Future)
    graph: dict = Field(default_factory=dict)

    # Index Stage (Future)
    index: RepositoryIndex | None = None

    # Documentation Stage (Future)
    documentation: dict[str, str] = Field(default_factory=dict)

    # Metadata
    metadata: dict = Field(default_factory=dict)
    
    symbols: RepositorySymbols | None = None
    
    