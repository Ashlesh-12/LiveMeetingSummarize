import streamlit as st
st.title("My App with Navigation")
## side bar
page=st.sidebar.selectbox("Go To",["Home","Dashboard","Settings"])

if page=="Home":
    st.header("Welcome to Home")
    st.write("This is the home page content")
elif page=="Dashboard":
    st.header("Dashboard")
    st.write("Charts,graphs,and metrics go here")
elif page=="Settings":
    st.header("Settings")
    st.write("Change your app preferences here")