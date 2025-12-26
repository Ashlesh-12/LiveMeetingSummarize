import streamlit as st
from PIL import Image

st.title("Image Display Example")

# Use the full path to your image
img = Image.open(r"C:\Users\nikhi\OneDrive\Pictures\Screenshots 1\sample.png")

st.image(img, caption="My Image", use_container_width=True)
