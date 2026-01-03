import streamlit as st
import base64

st.title("Upload and Display File Example")

uploaded_file = st.file_uploader("Upload an image or PDF", type=["pdf"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        st.write("PDF Uploaded Successfully!")
        
        base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    else:
        st.error("Unsupported file type!")
