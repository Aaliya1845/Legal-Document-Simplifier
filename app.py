import streamlit as st
from modules.pdf_reader import extract_pdf_text
from modules.docx_reader import extract_docx_text
from modules.utils import extract_txt_text
from modules.summarizer import summarize_document
from modules.simplifier import simplify_document

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

    st.markdown('<p class="main-title">⚖️ Legal Document Simplifier</p>', unsafe_allow_html=True)

    st.markdown(
        '<p class="sub-title">Understand complex legal documents in plain language using AI.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🚀 Features")
        st.success("✔ Upload PDF/DOCX/TXT")
        st.success("✔ AI Summary")
        st.success("✔ Simplify Legal Language")
        st.success("✔ Explain Clauses")
        st.success("✔ AI Chat")
        st.success("✔ Translate")
        st.success("✔ Download Results")

    with col2:
        st.info(
            """
            **How it works**

            1. Upload your legal document.
            2. AI extracts the text.
            3. Generate a summary.
            4. Simplify difficult legal terms.
            5. Ask questions about the document.
            6. Download the results.
            """
        )

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

        if "simplified" in st.session_state:

            st.success("Document simplified successfully!")

            st.markdown(st.session_state["simplified"])

            st.download_button(
                label="📥 Download Simplified Document",
                data=st.session_state["simplified"],
                file_name="simplified_document.txt",
                mime="text/plain"
            )

elif menu == "AI Chat":
    st.header("💬 AI Chat")
    st.info("Coming in the next step.")

elif menu == "Translate":
    st.header("🌍 Translate")
    st.info("Coming in the next step.")

elif menu == "History":
    st.header("🕒 History")
    st.info("Coming in the next step.")

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
