# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:26:51 2019

@author: user
"""

Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""
newstr=input("enter the name>")
dir(str)
help(str.upper)
newstr2=newstr.upper()
print(newstr)
print(newstr2)
help(str.lower)
newstr3=newstr.lower()
print(newstr3)
help(str.title)
newstr4=newstr.title
print(newstr4)