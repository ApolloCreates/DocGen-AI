from pathlib import Path


ENTRY_POINTS = {

    "main.py",

    "app.py",

    "manage.py",

    "run.py",

    "__main__.py",
}


class EntryPointDiscovery:

    def discover(self, root: Path):

        found = []

        for path in root.rglob("*"):

            if path.is_file() and path.name in ENTRY_POINTS:

                found.append(
                    str(path.relative_to(root))
                )

        return sorted(found)