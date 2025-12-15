from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
nltk.download("omw-1.4")  

lemmatizer=WordNetLemmatizer()

print("rocks :",lemmatizer.lemmatize("rocks"))
print("corpora :",lemmatizer.lemmatize("corpora"))

print("better :",lemmatizer.lemmatize("better",pos="a"))