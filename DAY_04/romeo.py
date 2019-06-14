# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:48:34 2019

@author: user
"""


"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
dict1={}
with open("romeo.txt","rt") as rf:
    filewords=rf.read().split()
    print(filewords)
    for word in filewords:
        print(word)
        if word in dict1.keys():
            dict1[word]+=1
        else:
            dict1[word]=1
print(dict1)
        
        
    
    



