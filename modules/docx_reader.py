"""
docx_reader.py
Extract text from Microsoft Word documents.
"""

from docx import Document


def extract_docx_text(uploaded_file):
    """
    Extract text from DOCX.

    Parameters:
        uploaded_file

    Returns:
        str
    """

    try:

        document = Document(uploaded_file)

        text = []

        for paragraph in document.paragraphs:
            text.append(paragraph.text)

        return "\n".join(text).strip()

    except Exception as e:
        return f"Error reading DOCX: {e}"
