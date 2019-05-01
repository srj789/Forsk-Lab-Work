# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:25:13 2019

@author: Suraj  kumar
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import json
import requests as re
api_key = "b35975e18dc93725acb092f7272cc6b8"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name  : ")
url = base_url + "appid=" + api_key + "&q=" + city_name
response=re.get(url)
x = response.json()
x
long=x['coord']
longitude=long['lon']
latitude=long['lat']
weather=x['weather']
weather=weather[0]['description']
windspeed=x['wind']
windspeed=windspeed['speed']
sun=x['sys']
sunrise=sun['sunrise']
sunset=sun['sunset']
print("Latitude          :",latitude)
print("Longitude         :",longitude)
print("Weather condition :",weather)
print("Wind speed (m/s)  :",windspeed)
print("SunRise time      :",sunrise)
print("SunSet time       :",sunset)
