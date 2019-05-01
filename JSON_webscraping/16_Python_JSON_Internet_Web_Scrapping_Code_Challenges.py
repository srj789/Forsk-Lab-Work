"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json
faculty={}
faculty['suraj']={
        'First Name':'Suraj',
        'Last Name':'Kumar',
        'Photo':'www.dsfssmmfk.com',
        'Department':'Cse',
        'Research Areas':['machine learning','Deep learning'],
        'Contact details':{'mob':'9087654321','email':'er.srj789@gmail.com'}
        }
faculty['aman']={
        'First Name':'aman',
        'Last Name':'Kumar',
        'Photo':'www.dsfsfk.com',
        'Department':'mechnaical',
        'Research Areas':['mototrs','animation'],
        'Contact details':{'mob':'2143567654','email':'srtyf.9@gmail.com'}
        }
jsonfile=json.dumps(faculty)
jsonfile



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


"""
Code Challenge
  Name: 
    Posting of Data
  Filename: 
    httpbin.py
  Problem Statement:
    Create a client REST API that sends and receives some information from 
    the Server by calling server's REST API.
    You are expected to create two functions each for Sending and 
    Receiving data.
    You need to make two api calls, one with POST method for sending data 
    and the other with GET method to receive data
    All the communication i.e. sending and receiving of data with the 
    server has to be in JSON format
  Hint:
    Host: httpbin.org
    Port :  80
    Protocol : POST
    URI : /post
    Content-Length: 32 

    firstname=Chris&language=English
"""
import requests
import json
url="http://httpbin.org/post"
data={"firstname":"Chris","language":"English"}
data
def post_data(url,data):
    r1= requests.post(url=url,data=data,json=data)
    post_data=r1.json()
    return post_data
print(post_data(url,data))

url2="http://httpbin.org/get"
def get_data(url,data):
    r2=requests.get(url=url,params=data)
    get_data=r2.json()
    return get_data
print(get_data(url2,data))

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
df[0].to_csv("ICC_File.csv",sep='\t')

