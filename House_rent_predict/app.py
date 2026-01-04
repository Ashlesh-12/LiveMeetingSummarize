import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page Configuration
st.set_page_config(page_title="House Rent Predictor", layout="centered")

# Load the saved model and encoders
try:
    model = joblib.load('rent_model.pkl')
    le_city = joblib.load('le_city.pkl')
    le_furn = joblib.load('le_furn.pkl')
except FileNotFoundError:
    st.error("Model files not found! Please run 'model_train.py' first.")
    st.stop()

st.title("🏠 Monthly House Rent Predictor")
st.write("Adjust the details below to see the estimated rent.")

# Input Section
st.divider()

col1, col2 = st.columns(2)

with col1:
    # Dropdown for Location (City)
    city = st.selectbox("Select City", le_city.classes_)
    
    # Dropdown for Furnishing Status
    furnish = st.selectbox("Furnishing Status", le_furn.classes_)

with col2:
    # Slider for BHK
    bhk = st.slider("Select BHK", min_value=1, max_value=10, value=2)
    
    # Slider for Size (Sq Ft)
    size = st.slider("Area Size (Sq Ft)", min_value=100, max_value=10000, value=1000, step=50)

st.divider()

# Prediction Button
if st.button("Calculate Estimated Rent", type="primary", use_container_width=True):
    # Prepare Input Data
    city_encoded = le_city.transform([city])[0]
    furn_encoded = le_furn.transform([furnish])[0]
    
    input_data = np.array([[city_encoded, size, bhk, furn_encoded]])
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    # UI Output
    #st.balloons()
    st.subheader(f"Estimated Monthly Rent:")
    st.title(f"₹ {round(prediction, 2):,}")
    
    st.info("Note: This prediction is based on historical patterns in CSV data.")