import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data/real_estate_prices.csv")

X = data[["year"]]
y = data["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Future prediction
future_years = [[2025], [2026], [2027]]
future_prices = model.predict(future_years)

for year, price in zip(future_years, future_prices):
    print(f"Year {year[0]} → Predicted Price: {int(price)}")
