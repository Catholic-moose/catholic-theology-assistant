import streamlit as st
from scraper import scrape_catechism  # make sure scraper.py is in your repo

st.set_page_config(page_title="Catholic Theology Assistant", page_icon="✝️")
st.title("✝️ Catholic Theology Assistant")
st.write("Load the Catechism directly from the Vatican website and split it into chunks for later processing!")

# -------------------------
# Helper function to split text
# -------------------------
def split_text(text, chunk_size=500, overlap=50):
    """
    Split text into chunks of `chunk_size` words, with optional overlap.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# -------------------------
# Load Catechism button
# -------------------------
if st.button("Load Catechism from Vatican website"):
    with st.spinner("Loading Catechism, please wait..."):
        catechism_text = scrape_catechism()
    st.success("✅ Catechism loaded successfully!")

    # -------------------------
    # Split text into chunks
    # -------------------------
    chunks = split_text(catechism_text)
    st.write(f"Text split into {len(chunks)} chunks.")

    # Show preview of first 3 chunks
    for i, chunk in enumerate(chunks[:3]):
        st.write(f"**Chunk {i+1}:**")
        st.write(chunk[:500] + "...")  # show first 500 characters of each
