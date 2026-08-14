from app.context.models import (
    ModuleContext,
    ReadmeContext,
)


class ContextBuilder:

    def build_readme(self, repository):

        modules = []

        languages = set()

        total_classes = 0
        total_functions = 0

        for parsed in repository.parsed_files:

            languages.add(parsed.language)

            total_classes += len(parsed.classes)

            total_functions += len(parsed.functions)

            modules.append(

                ModuleContext(

                    path=parsed.path.replace(
                        str(repository.root) + "/",
                        "",
                    ),

                    classes=[
                        c.name
                        for c in parsed.classes
                    ],

                    functions=[
                        f.name
                        for f in parsed.functions
                    ],

                    imports=[
                        i.module
                        for i in parsed.imports
                    ],

                )

            )

        return ReadmeContext(

            project_name=repository.name,

            languages=sorted(languages),

            total_files=len(repository.parsed_files),

            total_classes=total_classes,

            total_functions=total_functions,

            modules=modules,

        )