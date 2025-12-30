import streamlit as st

st.title("My App with Navigation")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Go to",
    ["Home", "Dashboard", "Settings"]
)

# Page content
if page == "Home":
    st.header("Welcome to Home Page")
    st.write("This is the home page content 😊")

elif page == "Dashboard":
    st.header("Dashboard")
    st.write("Charts, graphs, and metrics go here.")

elif page == "Settings":
    st.header("Settings")
    st.write("Change your app preferences here.")

import streamlit as st

st.title("Simple Top Navigation")

# Top navigation
menu = st.radio(
    "Navigation",
    ["Home", "Dashboard", "Settings"],
    horizontal=True
)

# Page content
if menu == "Home":
    st.subheader("Home")
    st.write("Welcome!")

elif menu == "Dashboard":
    st.subheader("Dashboard")
    st.line_chart([1, 5, 2, 6, 2, 7])

elif menu == "Settings":
    st.subheader("Settings")
    st.write("Configure your app here.")


import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Top Navigation", layout="wide")

# Horizontal top menu
selected = option_menu(
    menu_title=None,  # hide menu title
    options=["Home", "Dashboard", "Settings"],
    icons=["house", "bar-chart", "gear"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Page content
if selected == "Home":
    st.header("Home Page")
    st.write("Welcome!")

elif selected == "Dashboard":
    st.header("Dashboard")
    st.line_chart([1, 5, 2, 6, 2, 7])

elif selected == "Settings":
    st.header("Settings")
    st.write("Configure your app here.")
