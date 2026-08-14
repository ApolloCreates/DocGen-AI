SUMMARY_PROMPT = """
You are a senior software engineer.

Write a professional project summary.

Use ONLY the information provided.

Do NOT invent features.

Repository Information:

{context}

Generate:

# Project Summary

Include:

- What the project is
- Main purpose
- Technologies used
- Key modules
- High-level workflow

Return Markdown only.
"""