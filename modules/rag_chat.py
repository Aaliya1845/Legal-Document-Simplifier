"""
RAG Chat System for Legal Document Q&A
"""

from modules.text_splitter import split_document
from modules.embeddings import model
from modules.vector_store import create_vector_store, search
from modules.gemini_client import generate_response
import numpy as np


class LegalRAGChat:

    def __init__(self, document_text):
        self.document_text = document_text
        self.chunks = None
        self.embeddings = None
        self.index = None
        self.chunk_embeddings = None

        self._build_index()

    def _build_index(self):

        # Step 1: Split document
        self.chunks = split_document(self.document_text)

        # Step 2: Create embeddings
        self.chunk_embeddings = model.encode(self.chunks)

        # Step 3: Create FAISS index
        self.index = create_vector_store(self.chunk_embeddings)

    def ask(self, question: str):

        try:
            # Step 1: Embed question
            question_embedding = model.encode([question])[0]

            # Step 2: Search relevant chunks
            indices = search(self.index, question_embedding, k=3)

            relevant_chunks = [
                self.chunks[i] for i in indices
            ]

            context = "\n\n".join(relevant_chunks)

            # Step 3: Build prompt
            prompt = f"""
You are a legal AI assistant.

Answer ONLY using the given document context.

If the answer is not in the context, say:
"I cannot find this information in the document."

Context:
{context}

Question:
{question}

Give a clear, simple answer.
"""

            # Step 4: Get response from Gemini
            response = generate_response(prompt)

            return response

        except Exception as e:
            return f"Error in RAG Chat: {e}"
