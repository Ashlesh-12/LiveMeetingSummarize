import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("heart_model.pkl", "rb"))

st.title("Heart Disease Prediction System")
st.write("⚠ For educational purposes only")

age = st.number_input("Age", 1, 120)
#sex = st.selectbox("Sex", [0,1])
sex = st.radio("Sex", ["Female", "Male"])
sex = 0 if sex == "Female" else 1
cp = st.number_input("Chest pain type (0-3)", 0, 3)
trestbps = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting blood sugar (>120 mg/dl)", [0,1])
restecg = st.selectbox("Rest ECG", [0,1,2])
thalach = st.number_input("Max heart rate")
exang = st.selectbox("Exercise induced angina", [0,1])
oldpeak = st.number_input("Oldpeak value")
slope = st.number_input("Slope", 0, 2)
ca = st.number_input("Number of major vessels (0–3)", 0, 3)
thal = st.number_input("Thal", 0, 3)

if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❗ High Risk: Possible Heart Disease")
    else:
        st.success("✔ Low Risk: No Heart Disease")
