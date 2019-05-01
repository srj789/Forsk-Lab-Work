"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
"""

import requests
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
html = requests.get(url).content
html
df = pd.read_html(html)
df
df
df[0].to_csv("ICC_File.csv",sep='\t')