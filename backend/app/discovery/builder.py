from app.discovery.models import DiscoveryResult

from app.discovery.framework import (
    detect_frameworks,
)

from app.discovery.package_manager import (
    detect_package_manager,
)

from app.discovery.dependencies import (
    detect_dependencies,
)

from app.discovery.entrypoints import (
    detect_entrypoints,
)

from app.discovery.configs import (
    detect_config_files,
)


class DiscoveryBuilder:

    def build(self, repository):

        return DiscoveryResult(

            frameworks=detect_frameworks(
                repository
            ),

            package_manager=detect_package_manager(
                repository.root
            ),

            dependencies=detect_dependencies(
                repository.root
            ),

            entry_points=detect_entrypoints(
                repository.root
            ),

            config_files=detect_config_files(
                repository.root
            ),

        )