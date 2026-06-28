"""
Split long legal documents into smaller chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_document(document_text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )

    chunks = splitter.split_text(document_text)

    return chunks
