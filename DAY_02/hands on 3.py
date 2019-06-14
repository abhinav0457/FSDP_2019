# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:19:05 2019

@author: user
"""

        
"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year
m=input("enter the month name> ")
def days_in_month(m):
    month=['january','march','may','july','august','october','december']
    if m in month:
        print("month has 31 days")
    else:
        print("month has 30 days")
        
days_in_month(m)       