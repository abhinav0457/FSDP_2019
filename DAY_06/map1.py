# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:28:59 2019

@author: user
"""


"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
      import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""
import random
dir(random)
help(random.choice)

import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

result=list(map(lambda i:random.choice(code_names),names))
