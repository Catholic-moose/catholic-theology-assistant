import streamlit as st
from scraper import scrape_catechism

st.set_page_config(page_title="Catholic Theology Assistant", page_icon="✝️")
st.title("✝️ Catholic Theology Assistant")
st.write("Load the Catechism directly from the Vatican website!")

if st.button("Load Catechism from Vatican website"):
    with st.spinner("Loading Catechism, please wait..."):
        catechism_text = scrape_catechism()
    st.success("✅ Catechism loaded successfully!")
    st.write(catechism_text[:2000] + "...")  # preview first 2000 characters
