# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:22:03 2019

@author: user
"""


# Code Challenge

"""
Research the below wesbite and post some data on it
https://requestbin.com
"""
import json
import requests

Host="https://enelj1n996gy.x.pipedream.net"

data = {"firstname":"dev","language":"English"}


headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

response=requests.post(Host,headers,data)
print(response)
