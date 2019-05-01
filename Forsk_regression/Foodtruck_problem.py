# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:14:43 2019

@author: Suraj  kumar
"""
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Forsk_problem_2/Foodtruck.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
print(regressor.score(X,y))

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population(in million)')
plt.ylabel('Profit')
plt.show()

print("Estimated profit/loss in jaipur")
val=3.073
y_pred = regressor.predict(val)
print(y_pred)
if(y_pred<0):
    print("Loss")
else:
    print("Profit")
