import streamlit as st
from streamlit_option_menu import option_menu

# Horizontal top menu
selected = option_menu(
    menu_title=None,  # hide the menu title
    options=["Home", "Dashboard", "Settings"],
    icons=["house", "bar-chart", "gear"],  # optional icons
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.header("Home Page")
    st.write("Welcome!")

elif selected == "Dashboard":
    st.header("Dashboard")
    st.line_chart([10, 20, 30, 25, 15])

elif selected == "Settings":
    st.header("Settings")
    st.write("App configuration here.")
