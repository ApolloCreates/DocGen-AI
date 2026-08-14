FRAMEWORKS = {
    "fastapi": "FastAPI",
    "flask": "Flask",
    "django": "Django",
    "streamlit": "Streamlit",
    "langgraph": "LangGraph",
    "langchain": "LangChain",
    "gradio": "Gradio",
    "reflex": "Reflex",
    "litestar": "Litestar",
    "sqlalchemy": "SQLAlchemy",
    "celery": "Celery",
}


def detect_frameworks(repository) -> list[str]:
    """
    Detect frameworks by inspecting parsed imports.
    """

    detected = set()

    for parsed in repository.parsed_files:

        for imp in parsed.imports:

            text = imp.module.lower()

            for key, framework in FRAMEWORKS.items():

                if key in text:

                    detected.add(framework)

    return sorted(detected)