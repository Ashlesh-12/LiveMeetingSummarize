# import these modules
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("mice :",lemmatizer.lemmatize("mice"))

# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos="a"))
