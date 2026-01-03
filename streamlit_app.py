import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit!")
st.write("This is my first Streamlit app.")

name = st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"Hello {name}! Welcome")

data=pd.DataFrame({"x":[1,2,3,4],"y":[10,20,30,40]})
st.line_chart(data)


st.title("Chart Example")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(data)

st.title("Sidebar Example")

option = st.sidebar.selectbox(
    "Choose a number",
    [10, 20, 30, 40]
)

st.write("You selected:", option)

from PIL import Image

st.title("Image Display")

img = Image.open("download.jpg")
st.image(img, use_container_width=True)

st.title("Live Text Display")

text = st.text_area("Type something")
st.write("You typed:")
st.write(text)

st.title("Sidebar Filters")

option = st.sidebar.selectbox("Choose a category", ["A", "B", "C"])
slider_val = st.sidebar.slider("Select a value", 1, 100)
flag = st.sidebar.checkbox("Enable feature")

st.write("Option:", option)
st.write("Slider:", slider_val)
st.write("Feature enabled:", flag)