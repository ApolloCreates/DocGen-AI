from pathlib import Path


class PackageManagerDiscovery:

    def discover(self, root: Path):

        if (root / "uv.lock").exists():
            return "uv"

        if (root / "poetry.lock").exists():
            return "poetry"

        if (root / "Pipfile").exists():
            return "pipenv"

        if (root / "requirements.txt").exists():
            return "pip"

        if (root / "package-lock.json").exists():
            return "npm"

        if (root / "pnpm-lock.yaml").exists():
            return "pnpm"

        if (root / "yarn.lock").exists():
            return "yarn"

        return None