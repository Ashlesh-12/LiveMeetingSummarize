import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data/real_estate_prices.csv")

X = data[['area', 'rooms']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

new_house = [[1600, 4]]
predicted_price = model.predict(new_house)

print("Predicted Property Price: ", int(predicted_price[0]))