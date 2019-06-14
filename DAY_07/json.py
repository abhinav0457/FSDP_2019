# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:37:02 2019

@author: user
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
import requests

url1="http://api.openweathermap.org/data/2.5/weather"
url2="?q=Jaipur"
url3="&appid=e9185b28e9969fb7a300801eb026de9c"

url=url1+url2+url3
print(url)

response=requests.get(url)
response.content

jsondata=response.json()
print(jsondata["coord"])
print(jsondata["weather"])
print(jsondata["wind"])
print(jsondata["sys"]["sunrise"])
print(jsondata["sys"]["sunset"])