# upload PDF in Streamlit
import streamlit as st
import base64

st.title("Upload and Display PDF")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    # Read PDF bytes
    pdf_bytes = uploaded_file.read()
    
    # Encode to base64
    b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    
    # Embed PDF in iframe
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="1000" type="application/pdf"></iframe>'
    
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    # Optional: Download button
    st.download_button(
        "Download PDF",
        data=pdf_bytes,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )




# Here’s a fully working Streamlit app that lets you upload and display an image:
import streamlit as st
from PIL import Image

# Title of the app
st.title("Upload and Display Image")

# File uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# If a file is uploaded, open and display it
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)


# Here's a code that will take pdf as input and display the summary of it

import streamlit as st
from PIL import Image
import PyPDF2  # <-- Make sure this line is included

st.title("Upload and Display Image or PDF")

# Allow images and PDFs
uploaded_file = st.file_uploader(
    "Upload an image or PDF",
    type=["jpg", "png", "jpeg", "pdf"]
)

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        # Handle PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        st.write(f"PDF has {len(pdf_reader.pages)} page(s)")
        # Display text from first page as an example
        first_page = pdf_reader.pages[0]
        text = first_page.extract_text()
        st.text_area("Text from first page", text, height=200)
    else:
        # Handle image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)
