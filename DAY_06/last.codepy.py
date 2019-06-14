# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:56:08 2019

@author: user
"""


"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""
list1=[1,2,3,4,5]
my_filter_list=list(filter(lambda i:i%2==1,list1))

from functools import reduce
reduce(lambda i,j:i*j,my_filter_list)