# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:10:35 2019

@author: user
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
user_input=input("enter the name of text file> ")
with open(user_input+".txt","rt") as rf:
     filecontent= rf.readlines()[-1]
    # position= rf.tell()
    # print(position)
     #line=rf.read(position)
     print(filecontent)
    
     

    
    
    