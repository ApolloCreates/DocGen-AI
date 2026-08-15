import re


def sanitize_mermaid(text: str) -> str:
    """
    Clean common Mermaid syntax mistakes produced by LLMs.
    """

    # Remove accidental markdown fences if present.
    text = re.sub(
        r"^\s*```mermaid\s*",
        "",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\s*```\s*$",
        "",
        text,
    )

    # Fix:
    #
    # A -->|label|> B
    #
    # into:
    #
    # A -->|label| B
    text = re.sub(
        r"\|>\s+",
        "| ",
        text,
    )

    # Fix accidental spaces around labelled arrows.
    #
    # A --> |label| B
    # becomes
    # A -->|label| B
    text = re.sub(
        r"-->\s+\|",
        "-->|",
        text,
    )

    return text.strip()