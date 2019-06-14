# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:16:09 2019

@author: user
"""



"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
my_list=['Monday', 'Wednesday', 'Thursday', 'Saturday']
user_input=input("enter the day> ")
for i in my_list:
    if i==user_input:
        break
    else:
        my_list=my_list.append('user_input')
print(tuple(my_list))        
        
#
my_tuple=('Monday', 'Wednesday', 'Thursday', 'Saturday')

new_tuple=(my_tuple[0],) + ('Tuesday',) + my_tuple[1:3] + ('friday',) + (my_tuple[-1])

print(new_tuple)