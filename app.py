import streamlit as st
import PyPDF2

# Page setup
st.set_page_config(page_title="Catholic Theology Assistant", page_icon="✝️")
st.title("✝️ Catholic Theology Research Assistant")
st.write("Upload PDFs to manage your Catholic documents!")

# -------------------------
# PASSWORD PROTECTION
# -------------------------
PASSWORD = "papist"  # <-- your password here

password_input = st.text_input("Enter password to upload PDFs:", type="password")

if password_input == PASSWORD:
    st.success("✅ Access granted. Upload your PDFs below.")

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

            # Optional: show first page preview
            try:
                reader = PyPDF2.PdfReader(pdf)
                first_page = reader.pages[0].extract_text()
                st.write(f"First page preview:\n{first_page[:300]}...")  # first 300 chars
            except:
                st.write("⚠️ Could not extract text from this PDF.")

else:
    if password_input:
        st.warning("⚠️ Incorrect password. Please try again.")
