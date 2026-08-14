from data.repos.fastapi.tests.test_ws_dependencies import index
from app.indexer.models import RepositoryIndex
class RepositoryIndexer:

    def build(self, repository):

        index = RepositoryIndex()

        index.files = repository.parsed_files

        index.total_files = len(
            repository.parsed_files
        )
        
        languages = {
            file.language
            for file in repository.parsed_files
        }
        
        index.file_tree = sorted(
            file.path
            for file in repository.files
        )

        index.languages = sorted(languages)
        
        for parsed in repository.parsed_files:

            index.total_classes += len(
                parsed.classes
            )

            index.total_functions += len(
                parsed.functions
            )

            index.total_imports += len(
                parsed.imports
            )

            index.total_endpoints += len(
                parsed.endpoints
            )

        return index