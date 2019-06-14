# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:13:32 2019

@author: user
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

#file =open("absentee.txt","wt")
#file.close()

n=0
with open("absentee.txt","wt") as file:
    while True:
        if(n<=25):
            user_input=input("enter the name of students>")
            if not user_input:
                break
        file.write(user_input+"\n")
        n=n+1
        
with open("absentee.txt","rt") as rf:
    filecontents=rf.read()
    print(filecontents)
    
      
      
      
      
      