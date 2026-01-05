import streamlit as st
import speech_recognition as sr
import numpy as np
from sentence_transformers import SentenceTransformer, util

# ------------------------------
# Streamlit Config
# ------------------------------
st.set_page_config(page_title="Voice to Sign", layout="centered")
st.title("🧏 Voice to Sign Language Translator")

# ------------------------------
# Load Model
# ------------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ------------------------------
# Letter to Sign Image Map
# ------------------------------
sign_map = {
    "A": "https://upload.wikimedia.org/wikipedia/commons/2/27/Sign_language_A.svg",
    "B": "https://upload.wikimedia.org/wikipedia/commons/1/18/Sign_language_B.svg",
    "C": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Sign_language_C.svg",
    "D": "https://upload.wikimedia.org/wikipedia/commons/0/06/Sign_language_D.svg",
    "E": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Sign_language_E.svg",
    "F": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Sign_language_F.svg",
    "G": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Sign_language_G.svg",
    "H": "https://upload.wikimedia.org/wikipedia/commons/9/97/Sign_language_H.svg",
    "I": "https://upload.wikimedia.org/wikipedia/commons/1/10/Sign_language_I.svg",
    "J": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Sign_language_J.svg",
    "K": "https://upload.wikimedia.org/wikipedia/commons/9/97/Sign_language_K.svg",
    "L": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Sign_language_L.svg",
    "M": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Sign_language_M.svg",
    "N": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Sign_language_N.svg",
    "O": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Sign_language_O.svg",
    "P": "https://upload.wikimedia.org/wikipedia/commons/0/08/Sign_language_P.svg",
    "Q": "https://upload.wikimedia.org/wikipedia/commons/3/34/Sign_language_Q.svg",
    "R": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Sign_language_R.svg",
    "S": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Sign_language_S.svg",
    "T": "https://upload.wikimedia.org/wikipedia/commons/1/13/Sign_language_T.svg",
    "U": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Sign_language_U.svg",
    "V": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Sign_language_V.svg",
    "W": "https://upload.wikimedia.org/wikipedia/commons/8/83/Sign_language_W.svg",
    "X": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Sign_language_X.svg",
    "Y": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Sign_language_Y.svg",
    "Z": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Sign_language_Z.svg"
}

# ------------------------------
# Phrase to Video Map
# ------------------------------
phrase_video_map = {
    "hello": "https://www.signingsavvy.com/media2/mp4-ld/24/24851.mp4",
    "thank you": "https://www.signingsavvy.com/media2/mp4-ld/24/24851.mp4",
    "how are you": "https://www.signingsavvy.com/media2/mp4-ld/33/33710.mp4",
    "my name is": "https://www.signingsavvy.com/media2/mp4-ld/22/22100.mp4",
    "please help me": "https://www.signingsavvy.com/media2/mp4-ld/33/33693.mp4",
    "what is your name": "https://www.signingsavvy.com/media2/mp4-ld/32/32333.mp4",
    "good morning": "https://www.signingsavvy.com/media2/mp4-ld/36/36746.mp4",
    "good evening": "https://www.signingsavvy.com/media2/mp4-ld/35/35816.mp4"
}

phrases = list(phrase_video_map.keys())
phrase_embeddings = model.encode(phrases)

# ------------------------------
# Helper: Show Letters
# ------------------------------
def show_letters(text):
    letters = [c for c in text.upper() if c.isalpha() and c in sign_map]
    if not letters:
        return
    cols = st.columns(len(letters))
    for col, letter in zip(cols, letters):
        col.image(sign_map[letter], width=50)

# ------------------------------
# MIC BUTTON
# ------------------------------
if st.button("🎤 Speak Now"):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            st.info("Listening...")
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio).lower()
        st.success(f"You said: {text}")

        matched_phrase = None
        for phrase in phrases:
            if phrase in text:
                matched_phrase = phrase
                break

        if matched_phrase:
            # rule-based logic
            start = text.find(matched_phrase)
            before = text[:start].strip()
            after = text[start + len(matched_phrase):].strip()

            if before:
                show_letters(before)

            st.video(phrase_video_map[matched_phrase])

            if after:
                show_letters(after)

        else:
            # SEMANTIC MATCH
            input_embedding = model.encode(text)
            similarities = util.cos_sim(input_embedding, phrase_embeddings)[0]
            best_idx = int(np.argmax(similarities))
            best_score = similarities[best_idx]

            st.write(f"Similarity score: {best_score:.2f}")

            if best_score >= 0.5:
               best_phrase = phrases[best_idx]

               # Split text into words
               text_words = text.split()
               phrase_words = best_phrase.split()

               # Remaining words not in phrase
               remaining_words = [w for w in text_words if w not in phrase_words]
               remaining_text = " ".join(remaining_words)

               # Show phrase video first
               st.video(phrase_video_map[best_phrase])

               # Then show remaining letters below video
               if remaining_text:
                  st.warning("Remaining words shown as letters:")
                  show_letters(remaining_text)
            else:
             st.warning("No phrase match found. Showing letters only.")
             show_letters(text)


    except sr.UnknownValueError:
        st.warning("I couldn't understand. Please speak again.")
    except sr.WaitTimeoutError:
        st.warning("No speech detected. Please try again.")
    except Exception:
        st.warning("Something went wrong. Please try again.")
