from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.schemas.repository import RepositoryAnalyzeRequest
from app.pipeline.repository import RepositoryPipeline
from pathlib import Path

from fastapi import HTTPException


router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
)

pipeline = RepositoryPipeline()


@router.post("/analyze")
def analyze(
    request: RepositoryAnalyzeRequest,
):
    try:

        repository = pipeline.run(
            str(request.url)
        )

        return {
            "repository": repository.name,
            "documents": list(
                repository.documentation.keys()
            ),
            "output_directory": (
                f"outputs/{repository.name}"
            ),
            "zip_file": repository.metadata.get(
                "documentation_zip"
            ),
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception:
        import traceback

        traceback.print_exc()

        raise
    
    

@router.get("/download/{repository_name}")
def download_documentation(
    repository_name: str,
):
    zip_path = (
        Path("outputs")
        / f"{repository_name}-docs.zip"
    )

    if not zip_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Documentation ZIP not found",
        )

    return FileResponse(
        path=zip_path,
        filename=f"{repository_name}-docs.zip",
        media_type="application/zip",
    )
    
    
@router.get(
    "/{repository_name}/documentation/{document_name}"
)
def get_documentation(
    repository_name: str,
    document_name: str,
):
    output_dir = (
        Path("outputs")
        / repository_name
    )

    file_path = output_dir / document_name

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Documentation file not found",
        )

    if file_path.suffix != ".md":
        raise HTTPException(
            status_code=400,
            detail="Only Markdown documents are supported",
        )

    return {
        "document": document_name,
        "content": file_path.read_text(
            encoding="utf-8"
        ),
    }