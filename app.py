import streamlit as st
import PyPDF2

st.title("✝️ Catholic Theology Research Assistant")
st.write("Upload PDFs to manage your Catholic documents!")

# PDF uploader
uploaded_files = st.file_uploader(
    "Choose PDF(s) to upload", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"✅ {len(uploaded_files)} PDF(s) uploaded successfully!")
    for pdf in uploaded_files:
        st.write(f"- {pdf.name}")
        # Optional: extract first page text
        reader = PyPDF2.PdfReader(pdf)
        first_page = reader.pages[0].extract_text()
        st.write(f"First page preview:\n{first_page[:300]}...")  # Show first 300 characters
