import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")  

stemmer = PorterStemmer()

input_file = "stemmer_input.txt"            
output_file = "stemmed_output.txt"  

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

words = word_tokenize(text)

stemmed_words = [stemmer.stem(word) for word in words]

stemmed_text = " ".join(stemmed_words)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(stemmed_text)

print("Stemming complete")
print(f"Input file   : {input_file}")
print(f"Output saved : {output_file}")
