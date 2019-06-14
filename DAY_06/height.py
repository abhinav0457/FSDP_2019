# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:32:25 2019

@author: user
"""


"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

      people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
  people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]
height_total=0
height_count=0
newlist=list(filter(lambda i:'height' in i,people))

newlist1=list(map(lambda a:a['height'],newlist))
from functools import reduce
newlist2=reduce(lambda x,y:(x+y)/len(newlist1),newlist1)
print(newlist2)

