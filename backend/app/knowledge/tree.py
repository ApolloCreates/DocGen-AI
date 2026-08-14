from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".next",
    "dist",
    "build",
}


def build_tree(root: Path) -> str:

    lines = [root.name + "/"]

    def walk(directory: Path, prefix: str = ""):

        entries = []

        for path in directory.iterdir():

            if path.name in IGNORED_DIRECTORIES:
                continue

            if path.name.startswith(".") and path.name not in {
                ".env.example",
            }:
                continue

            entries.append(path)

        entries.sort(
            key=lambda p: (
                p.is_file(),
                p.name.lower(),
            )
        )

        for index, path in enumerate(entries):

            is_last = index == len(entries) - 1

            connector = "└── " if is_last else "├── "

            if path.is_dir():

                lines.append(
                    prefix
                    + connector
                    + path.name
                    + "/"
                )

                next_prefix = (
                    prefix + "    "
                    if is_last
                    else prefix + "│   "
                )

                walk(path, next_prefix)

            else:

                lines.append(
                    prefix
                    + connector
                    + path.name
                )

    walk(root)

    return "\n".join(lines)