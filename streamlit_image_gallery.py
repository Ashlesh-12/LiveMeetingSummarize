import streamlit as st
from PIL import Image
col1, col2, col3=st.columns(3)

with col1:
    st.image(Image.open("download.jpg"))

with col2:
    st.image(Image.open("download.jpg"))

with col3:
    st.image(Image.open("download.jpg"))