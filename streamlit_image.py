import streamlit as st
from PIL import Image

st.title("Image Display Example")

img=Image.open("download.jpg")
st.image(img,caption="My Image",use_container_width=True)