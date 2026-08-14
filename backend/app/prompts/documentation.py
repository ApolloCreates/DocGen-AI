DOCUMENTATION_PROMPT = """
You are a senior software engineer and technical writer.

Generate documentation for the repository using ONLY the repository
analysis provided below.

STRICT RULES:
- Do not invent facts.
- Do not invent dependencies.
- Do not invent environment variables.
- Do not invent installation commands.
- Do not invent entry points.
- Do not infer the purpose of files merely from their names.
- Do not describe something as "likely", "probably", "appears to",
  or "suggests" unless the repository analysis explicitly supports it.
- If information is unavailable, say:
  "Not determined from the repository analysis."
- The repository tree is authoritative.
- Use only detected frameworks and dependencies from the context.

Return a JSON object with EXACTLY these four fields:

{{
  "readme": "...",
  "architecture": "...",
  "summary": "...",
  "installation": "..."
}}

Each field must contain valid Markdown.

README requirements:
# Project Overview
# Folder Structure
# Tech Stack
# Main Modules
# Installation
# Usage

ARCHITECTURE requirements:
# Architecture Overview
# High-Level Design
# Project Structure
# Execution Flow
# Module Relationships
# Technologies Used

SUMMARY requirements:
# Project Summary
Include:
- Purpose
- Main functionality
- Technologies
- Important modules
- High-level workflow

INSTALLATION requirements:
# Prerequisites
# Installation
# Running the Project
# Environment Variables

Only include information supported by the repository analysis.

Repository Analysis:

{context}
"""