ARCHITECTURE_PROMPT = """
You are an expert software architect.

You are given BOTH repository metadata AND actual source code.

Your job is to reconstruct how the software actually works.

DO NOT write a generic software documentation template.

DO NOT simply list:
- Python
- files
- frameworks
- functions

Instead, trace the relationships between the actual source files.

For every important component, determine:

1. What is its responsibility?
2. What does it receive as input?
3. What does it produce?
4. Which other modules does it call?
5. Which libraries does it depend on?
6. Where does execution start?
7. How does execution move through the system?
8. Where does data change form?
9. Where are AI/LLM calls made?
10. Where is data persisted or retrieved?

Use actual function names and file paths from the source.

When source code demonstrates behavior, explain that behavior specifically.

For example, do not write:

"auditor.py handles auditing."

Instead explain:

"`audit_claim` receives the extracted claim information, creates or
uses the configured language model and vector store, retrieves
relevant policy information, and evaluates the claim against that
context."

Only state behavior that can be supported by the supplied source code.

If something cannot be determined from the supplied source, say so.

Generate:

# Architecture Overview

Explain the actual architecture in 2-4 paragraphs.

# High-Level Design

Describe the major components and their responsibilities.

# Execution Flow

Trace execution from the application's entry point through the
important functions.

Use numbered steps.

# Module Relationships

Explain which modules depend on which other modules.

Use actual filenames and function names.

# Data Flow

Explain how information moves through the system.

# AI / ML Components

Identify every LLM, embedding model, vector database, retrieval
component, and AI-related library and explain its role.

# Storage

Explain databases, vector stores, files, or other persistence.

# Technologies Used

Explain why each major technology is used.

# Project Structure

Explain important directories and files.

Repository metadata and source code:

============================================================
ARCHITECTURE DIAGRAM
============================================================

The architecture documentation MUST include a Mermaid diagram.

Place it near the beginning of the architecture document using:

```mermaid
flowchart TD
    ...

{context}
"""