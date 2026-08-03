from pathlib import Path

FRAMEWORKS = {
    "fastapi": "FastAPI",
    "flask": "Flask",
    "django": "Django",
    "langgraph": "LangGraph",
    "streamlit": "Streamlit",
    "next": "Next.js",
    "react": "React",
}


def safe_read(path: Path) -> str:
    try:
        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        ).lower()
    except Exception:
        return ""


def detect_frameworks(root: Path) -> list[str]:

    frameworks = set()

    files = [

        "requirements.txt",

        "pyproject.toml",

        "package.json",

    ]

    for filename in files:

        path = root / filename

        if not path.exists():
            continue

        text = safe_read(path)

        for package, framework in FRAMEWORKS.items():

            if package in text:

                frameworks.add(framework)

    return sorted(frameworks)