from pathlib import Path


ENTRYPOINT_NAMES = {
    "main.py",
    "app.py",
    "server.py",
    "run.py",
    "manage.py",
    "cli.py",
}


def detect_entrypoints(root: Path) -> list[str]:
    """
    Detect likely application entrypoints.
    """

    entrypoints = []

    for file in root.rglob("*.py"):

        if file.name in ENTRYPOINT_NAMES:

            entrypoints.append(
                str(file.relative_to(root))
            )

    return sorted(entrypoints)