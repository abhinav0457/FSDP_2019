# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:36:16 2019

@author: user
"""

Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35

#score of assignments
 assignment1=float(input("enter the score of A1>"))
 assignment2=float(input("enter the score of A2>"))
 assignment3=float(input("enter the score of A3>"))
#score of exams
 exam1=float(input("enter the score 1"))
 exam2=float(input("enter the score 2"))
 #weighted score
 weighted_score=(assignment1+assignment2+assignment3)*0.1+(exam1+exam2)*0.35
 print(weighted_score)
 