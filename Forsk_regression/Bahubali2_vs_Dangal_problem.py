# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:57:34 2019

@author: Suraj  kumar
"""

import pandas as pd

dataset = pd.read_csv('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Forsk_problem_2/Bahubali2_vs_Dangal.csv')
X = dataset.iloc[:,:-2].values
y = dataset.iloc[:,1:-1].values
z = dataset.iloc[:,2]

from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(X, y)
print(regressor1.score(X,y))

regressor2 = LinearRegression()
regressor2.fit(X, z)
print(regressor2.score(X,z))

y_pred = regressor1.predict(10)
print("Bahubali2 collection",y_pred)
y_pred2 = regressor2.predict(10)
print("Dangal collection",y_pred2)

if(y_pred>y_pred2):
    print("Bahubali2 will collect more on 10th day")
else:
    print("Dangal movie will collect more on 10th day")