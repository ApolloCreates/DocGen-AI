from app.core.logger import logger

from app.pipeline.base import PipelineStage
from app.pipeline.context import RepositoryContext

from app.pipeline.stages.clone import CloneStage
from app.pipeline.stages.scan import ScanStage
from app.pipeline.stages.parse import ParseStage
from app.pipeline.stages.documentation import DocumentationStage
from app.pipeline.stages.index import IndexStage
from app.pipeline.stages.symbols import SymbolStage


class RepositoryPipeline:

    def __init__(self):

        self.stages: list[PipelineStage] = [

            CloneStage(),

            ScanStage(),

            ParseStage(),
            
            SymbolStage(),
            
            IndexStage(),
            
            DocumentationStage(),

        ]

    def run(self, url: str) -> RepositoryContext:

        if not url.strip():
            raise ValueError("Repository URL cannot be empty.")

        repository = RepositoryContext(
            url=url
        )

        logger.info(
            f"Starting pipeline for {url}"
        )

        for stage in self.stages:

            logger.info(
                f"Running {stage.__class__.__name__}"
            )

            repository = stage.run(
                repository
            )

        logger.info(
            "Repository pipeline completed successfully."
        )

        return repository