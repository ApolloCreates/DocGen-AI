from app.mapper.models import Module, RepositoryMap


class RepositoryMapper:

    def build(self, repository):

        repo_map = RepositoryMap()

        for parsed in repository.parsed_files:

            repo_map.modules.append(
                Module(
                    path=parsed.path,
                    imports=[i.module for i in parsed.imports],
                    classes=[c.name for c in parsed.classes],
                    functions=[f.name for f in parsed.functions],
                )
            )

        return repo_map