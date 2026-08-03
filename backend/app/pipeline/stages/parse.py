import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from app.core.logger import logger
from app.parser.service import ParserService
from app.pipeline.base import PipelineStage


class ParseStage(PipelineStage):

    def __init__(self):
        self.parser = ParserService()

    def parse_file(self, repository, file):
        return self.parser.analyze(
            repository.root / file.path
        )

    def run(self, repository):

        parsed_files = []

        total = len(repository.files)

        completed = 0

        workers = min(
            32,
            (os.cpu_count() or 4) * 2,
        )

        with ThreadPoolExecutor(
            max_workers=workers
        ) as executor:

            futures = {

                executor.submit(
                    self.parse_file,
                    repository,
                    file,
                ): file

                for file in repository.files

            }

            for future in as_completed(futures):

                completed += 1

                try:

                    result = future.result()

                    if result is not None:
                        parsed_files.append(result)

                except Exception as e:

                    logger.exception(
                        f"Failed to parse {futures[future].path}: {e}"
                    )

                logger.info(
                    f"Parsed {completed}/{total}"
                )

        repository.parsed_files = parsed_files

        return repository