import streamlit as st
from PIL import Image

st.title("Upload and Image Display Example")

uploaded_file=st.file_uploader("Upload an image",type=["jpg","png","jpeg"])

if uploaded_file:
    img=Image.open(uploaded_file)
    st.image(img,caption="Uploaded Image",use_container_width=True)
