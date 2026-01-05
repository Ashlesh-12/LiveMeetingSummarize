import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd

#Data Loading and Initial Print
data_set = pd.read_csv("/content/Experience-Salary.csv")

#Feature and Target Separation
x = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 1].values


#Data Splitting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)


#Model Training
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Prediction
y_pred = regressor.predict(x_test)
x_pred = regressor.predict(x_train) # Note: x_pred holds the predictions on the training data


#Training Set Visualization
mtp.scatter(x_train, y_train, color="green")
mtp.plot(x_train, x_pred, color="red")
mtp.title("Salary vs Experience (Training Dataset)")
mtp.xlabel("Years of Experience")
mtp.ylabel("Salary (In Rupees)")
mtp.show()

#Test Set Visualization
mtp.scatter(x_test, y_test, color='blue')
mtp.plot(x_train, x_pred, color='red')
mtp.title("Salary vs Experience (Test Dataset)")
mtp.xlabel("Years of Experience")
mtp.ylabel("Salary (In Rupees)")
mtp.show()
