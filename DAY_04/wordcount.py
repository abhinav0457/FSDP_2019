# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:11:35 2019

@author: user
"""


"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
user_input=input("enter the file name> ")
l=0
with open(user_input+".txt","rt") as rf:
    filecontent=rf.readline()
    print(len(filecontent))
    filecontent1=rf.readlines()
    print(len(filecontent1))
    
    #rf=rf.read().split()
    for i in filecontent:
        l +=len(i.split())
        print(l)
      

    
     