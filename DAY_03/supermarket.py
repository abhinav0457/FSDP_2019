# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:56:14 2019

@author: user
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
dict1 = {}
items_sold=[]
while True:
    user_input=input("enter the list of items>")
    if not user_input:
        break
    items_sold.append(user_input)
    user_input=user_input.split()
 if ' '.join(user_input[:-1]) in dict1:
        dict1[' '.join(str1[:-1])] = int(dict1[' '.join(user_input[:-1])])+int(user_input[-1])
        
    else:
        dict1[' '.join(user_input[:-1])]=user_input[-1]
print(items_sold)   
""" 
str1 = "BANANA FRIES 12"   
str1 = str1.split()
' '.join(str1[:-1])
str1[-1]
"""