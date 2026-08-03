from app.indexer.models import RepositoryIndex
from app.discovery.config_files import ConfigDiscovery
from app.discovery.config_files import ConfigDiscovery
from app.discovery.dependencies import DependencyDiscovery
from app.discovery.dependencies import DependencyDiscovery
from app.discovery.package_manager import PackageManagerDiscovery
from app.discovery.package_manager import PackageManagerDiscovery
from app.discovery.entrypoints import EntryPointDiscovery
from app.indexer.framework import detect_frameworks
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
        
        # index.frameworks = detect_frameworks(
        #     repository.root
        # )
        
        self.dependencies = DependencyDiscovery()
        self.entrypoints = EntryPointDiscovery()
        self.config = ConfigDiscovery()
        self.package_manager = PackageManagerDiscovery()


        # index.dependencies = self.dependencies.discover(
        #     repository.root
        # )

        # index.entry_points = self.entrypoints.discover(
        #     repository.root
        # )

        # index.config_files = self.config.discover(
        #     repository.root
        # )
    
        # index.package_manager = self.package_manager.discover(
        #     repository.root
        # )
        
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