# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:01:58 2019

@author: user
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
#1
list=[]
while True:
    user_input=input("enter the numbers>")
    if not user_input:
        break
    list.append(user_input)    
print(list)   
print(tuple(list))
    
#2
user_input=(input("enter the numbers> ")).split(",")
print(user_input)
print(tuple(user_input))