from modules.gemini_client import generate_response


def explain_clauses(document_text):
    """
    Explain each important legal clause in simple language.
    """

    prompt = f"""
You are an experienced legal expert.

Analyze the legal document below.

For every important clause provide:

1. Clause Title
2. Original Meaning
3. Simple Explanation
4. Rights
5. Responsibilities
6. Risks
7. Important Dates (if any)
8. Penalties (if any)

Use markdown headings and bullet points.

Document:

{document_text}
"""

    return generate_response(prompt)
