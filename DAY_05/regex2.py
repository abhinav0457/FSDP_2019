# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:28:49 2019

@author: user
"""


"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
import re
user_input=input("enter the email address> ").split()
list1=[]
for val in user_input:
    if re.findall(r'^[a-zA-Z]+\S\@\[a-z0-9]+\.\[a-z]{2,4}',val):
        list1.append(val)
print(list1)     

 ak=re.findall(r'^[a-zA-Z]+\@\[a-z0-9]+\.\w{2,4}', 'lara@hackerrank.com')
