FRAMEWORKS = {

    "fastapi": "FastAPI",

    "flask": "Flask",

    "django": "Django",

    "langgraph": "LangGraph",

    "streamlit": "Streamlit",

    "next": "Next.js",

    "react": "React",
}

from pathlib import Path


def detect_frameworks(root: Path):

    frameworks = set()

    requirements = root / "requirements.txt"

    if requirements.exists():

        text = requirements.read_text().lower()

        for package, framework in FRAMEWORKS.items():

            if package in text:

                frameworks.add(framework)

    return sorted(frameworks)