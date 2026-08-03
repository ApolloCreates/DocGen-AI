from app.context.models import ReadmeContext


class ContextBuilder:

    def build_readme(self, repository):

        index = repository.index

        classes = []
        functions = []

        for parsed in index.files:

            classes.extend(
                c.name
                for c in parsed.classes
            )

            functions.extend(
                f.name
                for f in parsed.functions
            )

        return ReadmeContext(

            project_name=repository.name,

            frameworks=index.frameworks,

            languages=index.languages,

            total_files=index.total_files,

            total_classes=index.total_classes,

            total_functions=index.total_functions,

            total_endpoints=index.total_endpoints,

            dependencies=index.dependencies,

            package_manager=index.package_manager,

            entry_points=index.entry_points,

            file_tree=index.file_tree,

            sample_classes=classes[:10],

            sample_functions=functions[:20],
        )