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