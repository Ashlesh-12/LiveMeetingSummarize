import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Cat vs Dog Classifier")
st.title("🐱🐶 Cat vs Dog Image Classifier")
st.write("Lightweight version – works on 4GB RAM")

uploaded_file = st.file_uploader(
    "Upload a cat or dog image",
    type=["jpg", "jpeg", "png"]
)

def classify_cat_dog(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (256, 256))

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.sum(edges > 0) / edges.size

    # Texture variance
    variance = np.var(gray)

    # Simple rule-based decision
    if edge_density > 0.08 and variance > 500:
        return "🐱 Cat"
    else:
        return "🐶 Dog"

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", width=500)

    prediction = classify_cat_dog(image_np)

    st.subheader("Prediction")
    st.success(prediction)
