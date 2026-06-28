"""
pdf_reader.py
Extract text from PDF files using PyMuPDF.
"""

import fitz  # PyMuPDF


def extract_pdf_text(uploaded_file):
    """
    Extract text from an uploaded PDF file.

    Parameters:
        uploaded_file (UploadedFile): Streamlit uploaded PDF.

    Returns:
        str: Extracted text.
    """

    try:
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text.strip()

    except Exception as e:
        return f"Error reading PDF: {e}"
