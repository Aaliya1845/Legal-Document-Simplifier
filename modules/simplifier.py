from modules.gemini_client import generate_response


def simplify_document(document_text):
    """
    Convert complex legal language into simple English.
    """

    prompt = f"""
You are an expert lawyer and legal educator.

Rewrite the following legal document in very simple English.

Rules:

- Preserve the original meaning.
- Use everyday language.
- Explain difficult legal words.
- Keep headings if present.
- Use bullet points where appropriate.
- Do NOT omit important information.
- Make it understandable for someone with no legal background.

Legal Document:

{document_text}
"""

    return generate_response(prompt)
