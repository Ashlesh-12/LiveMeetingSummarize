import streamlit as st
import joblib
import numpy as np

st.title("Student Performance Prediction System")

log_model = joblib.load("model_pass_fail.pkl")
lin_model = joblib.load("model_marks.pkl")

study = st.number_input("Study Hours")
attendance = st.number_input("Attendance (%)")
internal = st.number_input("Internal Marks")

if st.button("Predict Pass/Fail"):
    data = np.array([[study, attendance, internal]])
    result = log_model.predict(data)[0]
    if result == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")

if st.button("Predict Final Marks"):
    data = np.array([[study, attendance, internal]])
    marks = lin_model.predict(data)[0]
    st.info(f"Predicted Final Marks: {marks:.2f}")
