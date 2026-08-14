from app.knowledge.models import (
    ModuleKnowledge,
    RepositoryKnowledge,
    RepositoryStatistics,
)
from app.knowledge.tree import build_tree


class KnowledgeBuilder:

    def build(self, repository):

        modules = []

        languages = set()

        total_classes = 0

        total_functions = 0

        for parsed in repository.parsed_files:

            languages.add(parsed.language)

            total_classes += len(parsed.classes)

            total_functions += len(parsed.functions)

            modules.append(

                ModuleKnowledge(

                    path=parsed.path.replace(
                        str(repository.root) + "/",
                        "",
                    ),

                    language=parsed.language,

                    imports=[
                        i.module
                        for i in parsed.imports
                    ],

                    classes=[
                        c.name
                        for c in parsed.classes
                    ],

                    functions=[
                        f.name
                        for f in parsed.functions
                    ],

                )

            )

        # Discovery is optional for now
        discovery = repository.discovery

        frameworks = (
            discovery.frameworks
            if discovery
            else []
        )

        dependencies = (
            discovery.dependencies
            if discovery
            else []
        )

        entry_points = (
            discovery.entry_points
            if discovery
            else []
        )

        package_manager = (
            discovery.package_manager
            if discovery
            else None
        )
        
        tree = build_tree(repository.root)

        return RepositoryKnowledge(
            project_name=repository.name,

            languages=sorted(languages),

            frameworks=frameworks,

            dependencies=dependencies,

            entry_points=entry_points,

            config_files=(
                discovery.config_files
                if discovery
                else []
            ),

            package_manager=package_manager,

            tree=tree,

            statistics=RepositoryStatistics(
                total_files=len(repository.parsed_files),
                total_classes=total_classes,
                total_functions=total_functions,
            ),

            modules=modules,
        )