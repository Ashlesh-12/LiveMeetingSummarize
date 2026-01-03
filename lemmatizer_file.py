import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

input_file = "input.txt"
output_file = "lemmatized_output.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

words = word_tokenize(text)

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

lemmatized_text = " ".join(lemmatized_words)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(lemmatized_text)

print("Lemmatization complete")
print("Output saved to:", output_file)
