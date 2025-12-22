import streamlit as st
import pickle
from preprocess import clean_text

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="Sentiment Analysis", page_icon="💬")
st.title("💬 Sentiment Analysis App")
st.write("Enter a review or tweet to analyze sentiment")

user_input = st.text_area("Enter text here")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        cleaned_text = clean_text(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]

        if prediction == 1:
            st.success("🟢 Positive Sentiment")
        elif prediction == 0:
            st.info("🟡 Neutral Sentiment")
        else:
            st.error("🔴 Negative Sentiment")
