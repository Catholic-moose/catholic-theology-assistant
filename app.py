import streamlit as st
import PyPDF2

st.title("✝️ Catholic Theology Research Assistant")

# -------------------------
# PASSWORD PROTECTION
# -------------------------
PASSWORD = "mysecret123"  # <-- change to your own

password_input = st.text_input("Enter password to upload PDFs:", type="password")

if password_input == PASSWORD:
    st.write("✅ Access granted. Upload your PDFs below.")

    uploaded_files = st.file_uploader(
        "Choose PDF(s) to upload", 
        type="pdf", 
        accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"✅ {len(uploaded_files)} PDF(s) uploaded successfully!")
        for pdf in uploaded_files:
            st.write(f"- {pdf.name}")
else:
    st.warning("⚠️ Enter the correct password to upload PDFs.")
