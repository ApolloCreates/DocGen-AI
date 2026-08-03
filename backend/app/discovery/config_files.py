from pathlib import Path


CONFIG_FILES = {

    ".env.example",

    "Dockerfile",

    "docker-compose.yml",

    "docker-compose.yaml",

    "pyproject.toml",

    "requirements.txt",

    "package.json",

    "README.md",
}


class ConfigDiscovery:

    def discover(self, root: Path):

        configs = []

        for path in root.rglob("*"):

            if path.name in CONFIG_FILES:

                configs.append(
                    str(path.relative_to(root))
                )

        return sorted(configs)