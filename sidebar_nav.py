import streamlit as st

st.title("My App with Navigation")

# Sidebar for navigation
page = st.sidebar.selectbox("Go to", ["Home", "Dashboard", "Settings"])

# Show content based on selection
if page == "Home":
    st.header("Welcome to Home")
    st.write("This is the home page content.")  # Correct comment placement

elif page == "Dashboard":
    st.header("Dashboard")
    st.write("Charts, graphs, and metrics go here.")

elif page == "Settings":
    st.header("Settings")
    st.write("Change your app preferences here.")
