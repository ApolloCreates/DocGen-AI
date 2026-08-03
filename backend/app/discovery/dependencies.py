from pathlib import Path


class DependencyDiscovery:

    def discover(self, root: Path) -> list[str]:

        dependencies = []

        requirements = root / "requirements.txt"

        if requirements.exists():

            for line in requirements.read_text().splitlines():

                line = line.strip()

                if (
                    not line
                    or line.startswith("#")
                ):
                    continue

                package = (
                    line.split("==")[0]
                    .split(">=")[0]
                    .split("<=")[0]
                    .strip()
                )

                dependencies.append(package)

        return sorted(dependencies)