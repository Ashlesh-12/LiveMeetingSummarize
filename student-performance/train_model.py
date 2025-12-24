import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("dataset.csv")

print("Columns loaded:", df.columns)
print(df)

# Features
X = df[['study_hours','attendance','internal_marks']]

# Target variables
y_pass = df['pass_fail']
y_marks = df['final_marks']

# Train Logistic Regression (Pass/Fail)
if len(df) > 2:   # prevents crash with low data
    X_train, X_test, y_train, y_test = train_test_split(X, y_pass, test_size=0.2)

    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)

    print("Pass/Fail model saved")
else:
    log_model = LogisticRegression()
    log_model.fit(X, y_pass)
    print("Pass/Fail model trained without split (low dataset)")

joblib.dump(log_model, "model_pass_fail.pkl")

# Train Linear Regression (Marks)
lin_model = LinearRegression()
lin_model.fit(X, y_marks)

joblib.dump(lin_model, "model_marks.pkl")

print("Models saved successfully!")
