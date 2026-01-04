import streamlit as st
import pickle
import PyPDF2
from preprocess import clean_text

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Function to read PDF
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# UI
st.title("📄 Resume Screening System")
st.write("Upload a resume and predict job role")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or TXT)",
    type=["pdf", "txt"]
)

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        resume_text = read_pdf(uploaded_file)
    else:
        resume_text = uploaded_file.read().decode("utf-8")

    cleaned = clean_text(resume_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)

    st.success(f"Predicted Job Role: {prediction[0]}")
