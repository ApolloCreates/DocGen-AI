README_PROMPT = """

STRICT ACCURACY RULES:

- Use only facts present in the repository context.
- Never invent dependencies.
- Never invent environment variables.
- Never invent installation commands.
- Never invent package managers.
- Never invent commands for running the application.
- If installation information is unavailable, explicitly say so.
- If environment variables are unavailable, omit that section.
- If the entry point is unknown, do not guess.
- The repository tree provided in the context is authoritative.
- Do not modify or reinterpret file names.


You are an expert software engineer.

Generate a professional README.md.

Use ONLY the repository information below.

Do NOT invent features.

If information is unavailable, omit that section.

Repository:

{context}

Generate these sections:

# Project Overview

# Folder Structure

# Tech Stack

# Main Modules

# Installation

# Usage

Return Markdown only.
"""