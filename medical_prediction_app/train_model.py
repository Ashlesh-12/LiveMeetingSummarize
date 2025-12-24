import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("heart.csv")

print(data.head())
print("Columns:", data.columns)

X = data.drop("condition", axis=1)   
y = data["condition"]                

# split dataset 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# save model
pickle.dump(model, open("heart_model.pkl", "wb"))

print("Model saved as heart_model.pkl")
