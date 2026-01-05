#pip install streamlit pillow

import streamlit as st
from PIL import Image
st.title("image display")
img=Image.open("sample.jpg")
st.img(img,caption="my img" , use_container_width=True)
