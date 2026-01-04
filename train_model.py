import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocess import clean_text

# Load dataset
df = pd.read_csv("dataset/resume_data.csv")

# Clean resume text
df["Resume"] = df["Resume"].apply(clean_text)

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Resume"])

# Labels
y = df["Category"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("✅ Model trained & saved successfully")
