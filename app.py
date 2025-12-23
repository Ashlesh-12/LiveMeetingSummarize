import streamlit as st
import pandas as pd

st.title("My first streamlit app")

data = pd.DataFrame({"x":[1,2,3,4],"y":[10,20,30,40]})
st.line_chart(data)