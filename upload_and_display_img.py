#pip install streamlit pillow

import streamlit as st
from PIL import Image
st.title("upload and display img")

uploaded_file = st.file_uploader("upload an img",type=["jpg", "png", "jpeg"])
if uploaded_file:
  img=Image.open(uploaded_file)
  st.image(img,caption="uploaded image", use_container_width=True)
