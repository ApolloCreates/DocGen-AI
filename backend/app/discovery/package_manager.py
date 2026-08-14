from pathlib import Path


def detect_package_manager(root: Path) -> str | None:
    """
    Detect the package manager used by the repository.
    """

    detectors = [
        ("uv.lock", "uv"),
        ("poetry.lock", "poetry"),
        ("Pipfile", "pipenv"),
        ("requirements.txt", "pip"),
        ("pyproject.toml", "pyproject"),
    ]

    for filename, manager in detectors:
        if (root / filename).exists():
            return manager

    return None