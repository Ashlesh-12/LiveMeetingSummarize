import streamlit as st

st.title("PDF Upload App")

uploaded_pdf = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_pdf is not None:
    st.success("PDF uploaded successfully!")
    
    st.write("File Name:", uploaded_pdf.name)
    st.write("File Size:", uploaded_pdf.size, "bytes")
