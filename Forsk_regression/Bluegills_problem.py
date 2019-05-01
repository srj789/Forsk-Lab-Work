# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 12:51:47 2019

@author: Suraj  kumar
"""
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Forsk_problem_2/bluegills.csv')

dataset.head()
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1:2]

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.score(X,y))

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
print(lin_reg_2.score(X_poly,y))


plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Age Vs Length (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Age vs Length (Polynomial Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()
