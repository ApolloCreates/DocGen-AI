from fastapi import APIRouter

from app.pipeline.repository import RepositoryPipeline
from app.schemas.repository import RepositoryAnalyzeRequest
router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
)

pipeline = RepositoryPipeline()

@router.post("/analyze")
def analyze(request: RepositoryAnalyzeRequest):

    return pipeline.run(str(request.url)).model_dump()

@router.post("/debug")
def debug_repository(request: RepositoryAnalyzeRequest):

    repository = pipeline.run(str(request.url))

    return {
        "files": len(repository.files),
        "parsed_files": len(repository.parsed_files),
        "first_file": (
            repository.parsed_files[0].model_dump()
            if repository.parsed_files
            else None
        ),
    }