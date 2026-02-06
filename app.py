import streamlit as st
import PyPDF2

st.set_page_config(page_title="Catholic Theology Assistant", page_icon="✝️")
st.title("✝️ Catholic Theology Assistant")
st.write("Upload a PDF of the Catechism and view its content in chunks!")

# -------------------------
# Helper function to extract PDF text
# -------------------------
def extract_pdf_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# -------------------------
# Helper function to split text
# -------------------------
def split_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# -------------------------
# PDF uploader
# -------------------------
uploaded_file = st.file_uploader("Upload a PDF of the Catechism", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        catechism_text = extract_pdf_text(uploaded_file)
    
    st.success("✅ PDF text extracted successfully!")
    st.write(f"Total characters extracted: {len(catechism_text)}")
    
    # Split text into chunks
    chunks = split_text(catechism_text)
    st.write(f"Text split into {len(chunks)} chunks.")
    
    # Preview first 3 chunks
    for i, chunk in enumerate(chunks[:3]):
        st.write(f"**Chunk {i+1}:**")
        st.write(chunk[:500] + "...")  # preview first 500 characters
