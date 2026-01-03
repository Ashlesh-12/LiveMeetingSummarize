import streamlit as st
from streamlit_option_menu import option_menu
# horizontal top menu
selected=option_menu(
    menu_title=None,
    options=["Home","Dashboard","Settings"],
    icons=["house","bar-chart","gear"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)
if selected=="Home":
    st.header("Welcome to Home")
    st.write("Welcome")
elif selected=="Dashboard":
    st.header("Dashboard")
    st.line_chart([10,20,30,25,15])
elif selected=="Settings":
    st.header("Settings")
    st.write("Configure your app here")
