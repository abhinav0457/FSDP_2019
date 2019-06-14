# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:36:35 2019

@author: user
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""


import re
user_input=input("enter the input> ").split()

for val in user_input:
    if re.findall(r'^[+-.]\d*\.\d+',val):
        print("True")
    else:
        print("false")


