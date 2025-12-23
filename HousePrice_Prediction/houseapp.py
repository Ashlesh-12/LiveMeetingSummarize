import streamlit as st
import pandas as pd
import cv2
import matplotlib.pyplot as plt

st.set_page_config(page_title="LiveMeetingAI", layout="wide")

st.title("RealtyAI Smart Real Estate Insight Platform")

data = pd.read_csv("data/real_estate_prices.csv")

st.subheader("Property Price Trend")
st.line_chart(data.set_index("year")["price"])

st.subheader("Property Data")
st.dataframe(data)

st.subheader("Satellite Image Segmentation")
img = cv2.imread("images/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, seg = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

fig, ax = plt.subplots()
ax.imshow(seg, cmap="gray")
ax.set_title("Segmented Image")
ax.axis("off")
st.pyplot(fig)

st.success("AI Analysis Completed Successfully")