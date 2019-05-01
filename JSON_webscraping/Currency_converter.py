# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:47:09 2019

@author: Suraj  kumar
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests as re
import json
code=input("Enter country currency code :") 
url="https://free.currconv.com/api/v7/convert?q=USD_"+code+"&compact=ultra&apiKey=84b52292fa683eb97bda"
response=re.get(url)
x = response.json()
x
