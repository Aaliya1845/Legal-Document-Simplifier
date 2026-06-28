import streamlit as st
st.markdown("""
<style>
.main-title {
    font-size: 44px;
    font-weight: 800;
    color: #1E88E5;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 20px;
}

.block {
    background-color: #f7f9fc;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #e0e0e0;
}
</style>
""", unsafe_allow_html=True)
init_db()
from modules.pdf_reader import extract_pdf_text
from modules.docx_reader import extract_docx_text
from modules.utils import extract_txt_text
from modules.summarizer import summarize_document
from modules.simplifier import simplify_document
from modules.clause_explainer import explain_clauses
from modules.rag_chat import LegalRAGChat
from modules.translator import translate_text
from modules.history import init_db, save_history, get_history

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Legal Document Simplifier",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-title{
    font-size:42px;
    font-weight:bold;
    color:#1E88E5;
}
.sub-title{
    font-size:20px;
    color:gray;
}
.feature-box{
    background:#F7F9FC;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚖️ Legal Document Simplifier")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Upload Document",
        "AI Summary",
        "Simplify",
        "Clause Explanation",
        "AI Chat",
        "Translate",
        "History",
        "About"
    ]
)

# -----------------------------
# Home
# -----------------------------
if menu == "Home":

    st.markdown('<div class="main-title">⚖ Legal Document Simplifier AI</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Upload • Understand • Simplify • Chat • Translate</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🚀 Features")

    st.markdown("""
    <div class="block">
    ✔ Upload PDF, DOCX, TXT<br>
    ✔ AI Summary<br>
    ✔ Legal Language Simplifier<br>
    ✔ Clause Explanation<br>
    ✔ AI Chat (RAG-based)<br>
    ✔ Translation<br>
    ✔ History Tracking
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧠 How it works")

    st.markdown("""
    <div class="block">
    1. Upload your legal document<br>
    2. AI extracts and understands it<br>
    3. Ask questions or simplify content<br>
    4. Download results anytime
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Upload
# -----------------------------
elif menu == "Upload Document":

    st.header("📄 Upload Legal Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX, or TXT file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        with st.spinner("Reading document..."):

            file_extension = uploaded_file.name.split(".")[-1].lower()

            if file_extension == "pdf":
                extracted_text = extract_pdf_text(uploaded_file)

            elif file_extension == "docx":
                extracted_text = extract_docx_text(uploaded_file)

            elif file_extension == "txt":
                extracted_text = extract_txt_text(uploaded_file)

            else:
                extracted_text = "Unsupported file format."

        st.success("✅ Document uploaded successfully!")

        st.session_state["document_text"] = extracted_text

        st.subheader("📑 Extracted Text")

        st.text_area(
            "Document Content",
            extracted_text,
            height=350
        )

        st.info(f"Total Characters: {len(extracted_text)}")

# -----------------------------
# Placeholder Pages
# -----------------------------
elif menu == "AI Summary":

    st.header("📖 AI Summary")

    if "document_text" not in st.session_state:
        st.warning("Please upload a document first.")

    else:

        if st.button("Generate Summary"):

            with st.spinner("Generating AI Summary..."):

                summary = summarize_document(
                    st.session_state["document_text"]
                )

                st.session_state["summary"] = summary
                save_history("Summary Generated", summary)

        if "summary" in st.session_state:

            st.markdown(st.session_state["summary"])

elif menu == "Simplify":
    st.header("✍ Simplify Legal Language")
    st.info("Coming in the next step.")

elif menu == "Simplify":

    st.header("✍️ Simplify Legal Document")

    if "document_text" not in st.session_state:

        st.warning("Please upload a document first.")

    else:

        if st.button("Simplify Document"):

            with st.spinner("Simplifying legal language..."):

                simplified = simplify_document(
                    st.session_state["document_text"]
                )

                st.session_state["simplified"] = simplified
               save_history("Document Simplified", simplified) 

        if "simplified" in st.session_state:

            st.success("Document simplified successfully!")

            st.markdown(st.session_state["simplified"])

            st.download_button(
                label="📥 Download Simplified Document",
                data=st.session_state["simplified"],
                file_name="simplified_document.txt",
                mime="text/plain"
            )
elif menu == "Clause Explanation":

    st.header("⚖️ Clause Explanation")

    if "document_text" not in st.session_state:

        st.warning("Please upload a document first.")

    else:

        if st.button("Explain Clauses"):

            with st.spinner("Analyzing clauses..."):

                explanation = explain_clauses(
                    st.session_state["document_text"]
                )

                st.session_state["clause_explanation"] = explanation
                save_history("Clause Explanation Generated", explanation)

        if "clause_explanation" in st.session_state:

            st.markdown(
                st.session_state["clause_explanation"]
            )

            st.download_button(
                "📥 Download Explanation",
                st.session_state["clause_explanation"],
                file_name="clause_explanation.txt",
                mime="text/plain"
            )
elif menu == "AI Chat":

    st.header("💬 AI Chat (Ask about your document)")

    if "document_text" not in st.session_state:
        st.warning("Please upload a document first.")

    else:

        # Initialize RAG system once
        if "rag_chat" not in st.session_state:
            with st.spinner("Preparing AI brain..."):
                st.session_state.rag_chat = LegalRAGChat(
                    st.session_state["document_text"]
                )

        user_question = st.text_input("Ask a question about your document")

        if st.button("Ask AI") and user_question:

            with st.spinner("Thinking..."):
                answer = st.session_state.rag_chat.ask(user_question)
                save_history("Chat Question", user_question)
save_history("Chat Answer", answer)

            st.markdown("### 🤖 Answer")
            st.write(answer)

elif menu == "Translate":

    st.header("🌍 Translate Document")

    if "document_text" not in st.session_state:
        st.warning("Please upload a document first.")

    else:

        text_to_translate = st.text_area(
            "Text to Translate",
            st.session_state["document_text"],
            height=300
        )

        language = st.selectbox(
            "Select Language",
            ["English", "Hindi", "Marathi", "Urdu", "Gujarati", "Bengali"]
        )

        if st.button("Translate"):

            with st.spinner("Translating..."):

                translated = translate_text(
                    text_to_translate,
                    language
                )

                st.session_state["translation"] = translated
                save_history("Translation", translated)

        if "translation" in st.session_state:

            st.markdown("### 🌍 Translated Output")
            st.write(st.session_state["translation"])

            st.download_button(
                "📥 Download Translation",
                st.session_state["translation"],
                file_name=f"translation_{language}.txt",
                mime="text/plain"
            )

elif menu == "History":

    st.header("🕒 Activity History")

    history = get_history()

    if not history:
        st.info("No history found.")
    else:
        for row in history:
            st.write(f"**{row[1]}**")
            st.write(row[2])
            st.caption(row[3])
            st.divider()

elif menu == "About":
    st.header("ℹ️ About")
    st.write(
        """
        **Legal Document Simplifier**

        Version: 1.0

        Built with:
        - Streamlit
        - Python
        - Gemini AI
        """
    )
