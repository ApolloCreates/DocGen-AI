README_PROMPT = """
You are an expert software engineer.

Generate a professional README.md.

Rules:

- Do NOT invent features.
- Use ONLY the repository information below.
- If information is unavailable, omit that section.
- Return valid Markdown only.

Repository Information:

{context}

Include:

# Project Overview

# Features

# Tech Stack

# Project Statistics

# Installation

# Folder Structure
"""