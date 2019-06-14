# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:04:06 2019

@author: user
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
with open("newfile.txt","wt") as file:
     file.write("this is my first line")
     
with open("newfile.txt" ,"rt") as rf:
     with open("copy.txt" , "wt") as wf:
         for line in rf:
             wf.write(line)
             
    