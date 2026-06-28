import streamlit as st

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
        "Choose a document",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:
        st.success("File uploaded successfully!")
        st.write("Filename:", uploaded_file.name)
        st.write("File Type:", uploaded_file.type)

# -----------------------------
# Placeholder Pages
# -----------------------------
elif menu == "AI Summary":
    st.header("📖 AI Summary")
    st.info("Coming in the next step.")

elif menu == "Simplify":
    st.header("✍ Simplify Legal Language")
    st.info("Coming in the next step.")

elif menu == "Clause Explanation":
    st.header("⚖ Explain Clauses")
    st.info("Coming in the next step.")

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
