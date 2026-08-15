SUMMARY_PROMPT = """
You are analyzing a software repository for a developer.

Generate a concise but technically meaningful project summary.

Use repository structure, imports, functions, classes, frameworks,
dependencies and entry points to understand the project's purpose.

Do not simply repeat filenames.

Explain:

1. Project Purpose
2. Main Functionality
3. Core Components
4. Technologies
5. Important Modules
6. High-Level Workflow
7. Inputs and Outputs
8. External Services
9. Storage / Data Layer

Make reasonable technical inferences from the available evidence.

For example, if the repository contains:
- a Streamlit entry point
- LangGraph workflow orchestration
- an interviewer node
- an auditor node
- a librarian node
- Chroma
- HuggingFace embeddings
- Groq

you should explain how these components likely work together.

Only say something is unknown when there is genuinely insufficient
evidence.

Repository information:

{context}
"""