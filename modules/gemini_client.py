"""
gemini_client.py
Handles Gemini API configuration and text generation.
"""

import streamlit as st
import google.generativeai as genai


def configure_gemini():
    """Configure the Gemini API."""
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)


def generate_response(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the response.
    """

    try:
        configure_gemini()

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {e}"
