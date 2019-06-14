# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:36:09 2019

@author: user
"""

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""
def translate(string):
    consonants='bcdfghijklmnpqrstvwxyz'
    final_list=[]
    
    for ele in string:
        if ele in consonants:
            final_list.append(ele+"o"+ele)
        else:
            final_list.append(ele)
    return "".join(final_list)        
user_input=input("enter the string> ")
print(translate(user_input))
        
    

