import streamlit as st
from scraper import scrape_catechism, get_catechism_links

st.set_page_config(page_title="Catholic Theology Assistant", page_icon="✝️")
st.title("✝️ Catholic Theology Assistant")
st.write("Load the Catechism directly from the Vatican website and check scraper output!")

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
# Load Catechism button
# -------------------------
if st.button("Load Catechism from Vatican website"):
    with st.spinner("Checking links first..."):
        links = get_catechism_links()
        st.write(f"Found {len(links)} pages to scrape.")
        st.write("Here are the first 5 links:")
        st.write(links[:5])  # preview first 5 links

    with st.spinner("Loading Catechism text..."):
        catechism_text = scrape_catechism()
        st.write(f"Total characters scraped: {len(catechism_text)}")
        st.write("Preview of first 1000 characters:")
        st.write(catechism_text[:1000])

    # Split into chunks
    chunks = split_text(catechism_text)
    st.write(f"Text split into {len(chunks)} chunks.")

    # Show preview of first 3 chunks
    for i, chunk in enumerate(chunks[:3]):
        st.write(f"**Chunk {i+1}:**")
        st.write(chunk[:500] + "...")
