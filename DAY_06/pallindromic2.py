# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:08:40 2019

@author: user
"""



"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
#way1
user_input=input("enter the number with space> ").split(" ")
for integer in user_input:
    if(integer==integer[::-1]):
        print("true")
    else:
        print("false")

#way2
list(map(lambda x:True if x==x[::-1] else False,input().split(" ")))

#use if and any

c=any(True if x==x[::-1]and int(i)>0 else False for i in input().split(" "))

