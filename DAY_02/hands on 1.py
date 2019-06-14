# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:20:41 2019

@author: user
"""

"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 


our_list = list(range(1,20))
print(our_list)

 #for even numbers
evenlist=our_list[1:19:2]
print(evenlist)
 
 #for odd numbers
oddlist=our_list[0:20:2]
print(oddlist)
 