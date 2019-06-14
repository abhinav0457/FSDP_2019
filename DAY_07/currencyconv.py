# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:00:15 2019

@author: user
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
import requests
url1="http://free.currencyconverterapi.com/api/v5/convert"
url2="?q=USD_INR"
url3="&compact=ultra&apiKey=5bd5abd36bbaeb708174"

url=url1+url2+url3
response=requests.get(url)
response.content

jsondata=response.json()
print(jsondata["USD_INR"])
