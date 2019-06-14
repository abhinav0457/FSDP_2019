# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:40:43 2019

@author: user
"""

Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""
newstr=input("enter the string>")
newstr.find('R')
newstr2='R'+newstr[1:].replace('R','$')
print(newstr2)