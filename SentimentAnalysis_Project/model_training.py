import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean_text

def main():
    df = pd.read_csv("data/kindle_sentiment.csv")

    df["reviewText"] = df["reviewText"].apply(clean_text)

    x = df["reviewText"]
    y = df["rating"]   

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2)
    )

    x_train_tfidf = vectorizer.fit_transform(x_train)
    x_test_tfidf = vectorizer.transform(x_test)

    model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
    model.fit(x_train_tfidf, y_train)

    y_pred = model.predict(x_test_tfidf)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("model.pkl and vectorizer.pkl saved successfully")

if __name__ == "__main__":
    main()
