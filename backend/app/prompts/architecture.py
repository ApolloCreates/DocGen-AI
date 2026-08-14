ARCHITECTURE_PROMPT = """
You are an expert software architect.

Your task is to analyze the repository information below and generate a technical architecture document.

Rules:
- Use ONLY the information provided.
- Do NOT invent components, APIs, or technologies.
- If information is unavailable, explicitly state that it could not be determined.
- Return valid Markdown only.

Repository Information:

{context}

Generate the document using the following structure:

# Architecture Overview

Briefly describe the overall purpose of the application.

# High-Level Design

Explain the overall architecture (for example: modular, layered, event-driven, workflow-based, etc.) based only on the provided information.

# Project Structure

Describe the major modules.

For each module include:
- Responsibility
- Classes
- Functions
- External dependencies

# Execution Flow

Describe how the application starts and how execution flows between modules.

If the entry point cannot be determined, say so.

# Technologies Used

List all detected languages, frameworks and major libraries.

# Internal Module Relationships

Explain how modules interact using their imports and responsibilities.

# Statistics

Include:

- Total Files
- Total Classes
- Total Functions
- Languages

# Future Improvements

Suggest architectural improvements that would naturally fit this codebase.
Do not suggest technologies that are unrelated to the repository.

Return Markdown only.
"""