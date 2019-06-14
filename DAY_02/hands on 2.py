# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:42:39 2019

@author: user
"""

Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False 


"""
def leap_year(year):
    year = int(input("enter the year>"))
    print(year)
    if (year % 100 == 0)or(year % 400!= 0)or(year % 4 ==0):
        print("leap year")
    else :
        print("not a leap year")
    
leap_year(year)    

#way2

year=int(input("enter the year> "))
def leap_fun(year):
    if (year%400==0):
        if year%100==0:
            if year%4==0:
                print("leap year")
            else:
                print("not")
        else:
            print("leap")
    else:
        print("not")
        
leap_fun(year)        

    