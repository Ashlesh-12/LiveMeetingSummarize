import re
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download once
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

STOPWORDS = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # Remove special characters
    text = re.sub(r"[^a-z\s]", "", text)

    # Remove stopwords
    text = " ".join([w for w in text.split() if w not in STOPWORDS])

    # Lemmatization
    text = " ".join([lemmatizer.lemmatize(w) for w in text.split()])

    return text
