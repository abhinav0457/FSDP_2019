# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:18:32 2019

@author: user
"""


"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
user_input=input("enter the string> ")
def reverse(user_input):
    input1=user_input[::-1]
    print(input1)
reverse(user_input)    