"""
Simple AI-based translation using Gemini
"""

from modules.gemini_client import generate_response


def translate_text(text, target_language="English"):
    """
    Translate legal/simplified text into target language.
    """

    prompt = f"""
You are a professional translator.

Translate the following text into {target_language}.

Rules:
- Keep meaning accurate
- Use simple language
- Do not add extra information
- Maintain legal meaning if present

Text:
{text}
"""

    return generate_response(prompt)
