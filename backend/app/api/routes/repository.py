from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.agents.chat import ChatAgent
from app.knowledge.builder import KnowledgeBuilder
from app.knowledge.models import RepositoryKnowledge
from app.pipeline.repository import RepositoryPipeline
from app.schemas.chat import (
    RepositoryChatRequest,
    RepositoryChatResponse,
)
from app.schemas.repository import RepositoryAnalyzeRequest


router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
)


pipeline = RepositoryPipeline()

knowledge_builder = KnowledgeBuilder()

chat_agent = ChatAgent()

# Simple in-memory cache for the MVP.
# Key: repository name
# Value: generated repository knowledge
knowledge_cache: dict[str, RepositoryKnowledge] = {}


@router.post("/analyze")
def analyze(
    request: RepositoryAnalyzeRequest,
):
    try:

        repository = pipeline.run(
            str(request.url)
        )

        # Build repository knowledge for the chatbot.
        knowledge = knowledge_builder.build(
            repository
        )

        knowledge_cache[
            repository.name
        ] = knowledge

        languages = sorted(
            {
                parsed.language
                for parsed in repository.parsed_files
            }
        )

        total_classes = sum(
            len(parsed.classes)
            for parsed in repository.parsed_files
        )

        total_functions = sum(
            len(parsed.functions)
            for parsed in repository.parsed_files
        )

        return {
            "repository": repository.name,

            "documents": [
                "README.md",
                "ARCHITECTURE.md",
                "SUMMARY.md",
                "INSTALLATION.md",
            ],

            "statistics": {
                "total_files": len(
                    repository.parsed_files
                ),
                "total_classes": total_classes,
                "total_functions": total_functions,
                "total_endpoints": sum(
                    len(parsed.endpoints)
                    for parsed in repository.parsed_files
                ),
            },

            "languages": languages,

            "frameworks": (
                repository.discovery.frameworks
                if repository.discovery
                else []
            ),

            "output_directory": (
                repository.metadata.get(
                    "output_directory"
                )
            ),

            "zip_file": (
                repository.metadata.get(
                    "documentation_zip"
                )
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


@router.post(
    "/chat",
    response_model=RepositoryChatResponse,
)
def chat(
    request: RepositoryChatRequest,
):

    repository_name = request.repository.strip()

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty",
        )

    knowledge = knowledge_cache.get(
        repository_name
    )

    if knowledge is None:

        raise HTTPException(
            status_code=404,
            detail=(
                "Repository has not been analyzed "
                "in this session"
            ),
        )

    try:

        answer = chat_agent.answer(
            knowledge,
            question,
        )

        return RepositoryChatResponse(
            answer=answer
        )

    except Exception:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail="Failed to generate answer",
        )


@router.get(
    "/download/{repository_name}"
)
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
            detail=(
                "Only Markdown documents are supported"
            ),
        )

    return {
        "document": document_name,
        "content": file_path.read_text(
            encoding="utf-8"
        ),
    }