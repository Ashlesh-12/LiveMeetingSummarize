from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
import pickle

from train_data import train_sentences, train_labels

# Load base model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode sentences
X = model.encode(train_sentences)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X, train_labels)

# Save trained classifier
with open("intent_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved")
