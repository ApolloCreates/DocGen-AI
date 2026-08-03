from app.context.models import ReadmeContext
from backend.app.api.routes import repository


class ContextBuilder:

    def build_readme(self, repository):

        index = repository.index

        languages = sorted(
            {
                file.language
                for file in index.files
            }
        )
        
        classes = []

        functions = []

        for parsed in repository.index.files:

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

            file_tree=index.file_tree,

            total_files=index.total_files,

            total_classes=index.total_classes,

            total_functions=index.total_functions,

            total_endpoints=index.total_endpoints,

            languages=languages,
            
            sample_classes=classes[:5],
            
            sample_functions=functions[:5],
        )