from pathlib import Path


CONFIG_FILES = [
    ".env",
    ".env.example",
    ".gitignore",
    "pyproject.toml",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    "compose.yml",
    "compose.yaml",
    "package.json",
    "Makefile",
    "README.md",
]


def detect_config_files(root: Path) -> list[str]:
    """
    Return configuration files found at the repository root.
    """

    found = []

    for file in CONFIG_FILES:

        path = root / file

        if path.exists():
            found.append(file)

    return sorted(found)