import streamlit as st
from scraper import scrape_catechism  # this is the file we wrote earlier

st.title("✝️ Catholic Theology Assistant")
st.write("Load the Catechism directly from the Vatican website!")

# Button to load the Catechism
if st.button("Load Catechism from Vatican website"):
    with st.spinner("Loading Catechism, please wait..."):
        catechism_text = scrape_catechism()
    st.success("✅ Catechism loaded successfully!")

    # Show a preview
    st.write(catechism_text[:2000] + "...")  # first 2000 characters
