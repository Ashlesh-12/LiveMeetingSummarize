import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data/real_estate_prices.csv")

# Features and target
X = data[["area", "rooms"]]
y = data["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict new house price
new_house = [[1600, 4]]  # area, rooms
predicted_price = model.predict(new_house)

print("Predicted Property Price:", int(predicted_price[0]))