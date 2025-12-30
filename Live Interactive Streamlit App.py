import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Live Streamlit App", layout="wide")

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🚀 Live Streamlit Demo App")

# --------------------------------------------------
# Live Name Input
# --------------------------------------------------
name = st.text_input("Enter your name")
if name:
    st.success(f"Hello {name}! Welcome 👋")

# --------------------------------------------------
# LIVE Slider-Controlled Chart
# --------------------------------------------------
st.subheader("📊 Live Chart")

points = st.slider("Number of data points", 5, 50, 20)

data = pd.DataFrame(
    np.random.randn(points, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)

# --------------------------------------------------
# Sidebar Live Controls
# --------------------------------------------------
st.sidebar.header("⚙️ Sidebar Controls")

category = st.sidebar.selectbox("Choose category", ["A", "B", "C"])
multiplier = st.sidebar.slider("Value multiplier", 1, 10)
show_image = st.sidebar.checkbox("Show Google Image")

st.write("Selected Category:", category)
st.write("Multiplier:", multiplier)

# --------------------------------------------------
# LIVE Data Table
# --------------------------------------------------
st.subheader("📋 Live Data Table")

df = pd.DataFrame({
    "Values": np.arange(1, 6) * multiplier
})

st.table(df)

# --------------------------------------------------
# GOOGLE IMAGE FROM URL (ADDED)
# --------------------------------------------------
if show_image:
    st.subheader("🖼 Image from Google")

    image_url = st.text_input(
        "Paste Google Image URL",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1024px-React-icon.svg.png"
    )

    if image_url:
        st.image(image_url, use_container_width=True)

# --------------------------------------------------
# LIVE Text Display
# --------------------------------------------------
st.subheader("📝 Live Text Display")

text = st.text_area("Type something")
st.write("You typed:")
st.info(text)
