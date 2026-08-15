from pydantic import BaseModel, Field


class ImportSymbol(BaseModel):
    module: str


class ClassSymbol(BaseModel):
    name: str
    line: int


class FunctionSymbol(BaseModel):
    name: str
    line: int


class EndpointSymbol(BaseModel):
    method: str
    path: str
    function: str
    line: int


class ParsedFile(BaseModel):

    path: str

    language: str

    source: str = ""

    imports: list[ImportSymbol] = Field(
        default_factory=list
    )

    classes: list[ClassSymbol] = Field(
        default_factory=list
    )

    functions: list[FunctionSymbol] = Field(
        default_factory=list
    )

    endpoints: list[EndpointSymbol] = Field(
        default_factory=list
    )