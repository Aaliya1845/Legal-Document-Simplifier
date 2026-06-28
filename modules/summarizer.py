from modules.gemini_client import generate_response


def summarize_document(document_text):
    """
    Generate a concise summary of a legal document.
    """

    prompt = f"""
You are an expert legal assistant.

Summarize the following legal document in simple English.

Include:

1. Purpose
2. Main Parties
3. Important Dates
4. Key Responsibilities
5. Risks
6. Important Clauses

Document:

{document_text}
"""

    return generate_response(prompt)
