"""
Utility functions.
"""


def extract_txt_text(uploaded_file):
    """
    Extract text from TXT file.
    """

    try:
        return uploaded_file.read().decode("utf-8")

    except Exception as e:
        return f"Error reading TXT: {e}"
