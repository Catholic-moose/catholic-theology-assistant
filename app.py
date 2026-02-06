import streamlit as st
import PyPDF2
from sentence_transformers import SentenceTransformer
import chromadb

st.set_page_config(page_title="Catholic Theology Assistant", page_icon="✝️")
st.title("✝️ Catholic Theology Assistant")
st.write("Upload a PDF of the Catechism and ask questions about it!")

# -------------------------
# Helper: Extract text from PDF
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
# Helper: Split text into chunks
# -------------------------
def split_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# -------------------------
# Initialize Chroma and embeddings
# -------------------------
client = chromadb.Client()
collection = client.get_or_create_collection(name="catechism")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------
# PDF uploader
# -------------------------
uploaded_file = st.file_uploader("Upload a PDF of the Catechism", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        catechism_text = extract_pdf_text(uploaded_file)
    
    st.success("✅ PDF text extracted successfully!")
    st.write(f"Total characters extracted: {len(catechism_text)}")
    
    # Split into chunks
    chunks = split_text(catechism_text)
    st.write(f"Text split into {len(chunks)} chunks.")
    
    # Create embeddings and store in Chroma
    for i, chunk in enumerate(chunks):
        vector = embedder.encode(chunk).tolist()
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[vector]
        )
    st.success("✅ Chunks embedded and indexed!")

    # -------------------------
    # Ask questions
    # -------------------------
    question = st.text_input("Ask a question about the Catechism:")

    if question:
        query_vector = embedder.encode(question).tolist()
        results = collection.query(
            query_embeddings=[query_vector],
            n_results=3
        )
        st.subheader("Relevant passages:")
        for doc in results['documents'][0]:
            st.write(doc)
