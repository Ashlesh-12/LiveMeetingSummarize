from nltk.stem import PorterStemmer

porter_stemmer=PorterStemmer()

words=["running","jumps","happily","running","happily"]

stemmed_words=[porter_stemmer.stem(word) for word in words]

print("Original words:",words)
print("Stemmed words:",stemmed_words)