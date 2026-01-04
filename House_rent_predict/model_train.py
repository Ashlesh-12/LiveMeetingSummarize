import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# 1. Load Data
file_path = 'data/house_rent.csv'
if not os.path.exists(file_path):
    print(f"Error: {file_path} not found. Please place your CSV in the 'data' folder.")
else:
    df = pd.read_csv(file_path)

    # 2. Select Features based on your CSV columns
    # Features: BHK, Size, City (Location), Furnishing Status
    # Target: Rent
    features = ['City', 'Size', 'BHK', 'Furnishing Status']
    X = df[features]
    y = df['Rent']

    # 3. Encoding Categorical Data
    le_city = LabelEncoder()
    le_furn = LabelEncoder()

    X['City'] = le_city.fit_transform(X['City'])
    X['Furnishing Status'] = le_furn.fit_transform(X['Furnishing Status'])

    # 4. Train Random Forest Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # 5. Save Model and Encoders
    joblib.dump(model, 'rent_model.pkl')
    joblib.dump(le_city, 'le_city.pkl')
    joblib.dump(le_furn, 'le_furn.pkl')

    print("✅ Model trained and saved successfully!")
    print(f"Cities learned: {list(le_city.classes_)}")