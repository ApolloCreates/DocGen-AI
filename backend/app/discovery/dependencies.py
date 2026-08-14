from pathlib import Path


def detect_dependencies(root: Path) -> list[str]:

    dependencies = set()

    requirements = root / "requirements.txt"

    if requirements.exists():

        try:

            text = requirements.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            for line in text.splitlines():

                line = line.strip()

                if (
                    not line
                    or line.startswith("#")
                ):
                    continue

                package = (
                    line.replace(">=", "==")
                    .split("==")[0]
                    .strip()
                )

                dependencies.add(package)

        except Exception:

            pass

    return sorted(dependencies)