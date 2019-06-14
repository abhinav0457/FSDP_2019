# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:39:32 2019

@author: user
"""
"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
takinginput = input("enter the input>")
for i in range(1,4,+1):
    print('* '*i)
for i in range(5,0,-1):
    print('* '*i)

#way2
    
user_input=int(input("enter the value> "))
str1="* "
n=1
while(True):
    print(str1*n)
    n=n+1
    if n==user_input:
        break
n=user_input
while(True):
    print(str1*n)
    n=n-1
    if n==0:
        break
    
        
