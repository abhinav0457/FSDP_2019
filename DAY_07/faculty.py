# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:59:23 2019

@author: user
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json
json_string="""
{
	"faculty1": {
		"name": {
			"first name": "ram",
			"last name": "sharma"
		},
		"department": "cse",
		"research areas": ["python", "ml", "java", "android"],
		"contact details": {
			"phone number": ["234", "345", "456"],
			"email": ["abc @123gmail.com",
				"bcd @23gmail.com"
			]
		}
	},
	"faculty2": {
		"name": {
			"first name": "mohan",
			"last name": "diwedi"
		},
		"department": "cse",
		"research areas": ["python", "ml", "java", "android"],
		"contact details": {
			"phone number": ["234", "345", "456"],
			"email": ["abc @123.com ",
				"bcd23 @.com"
			]
		}
	}
}
"""
my_data=json.loads(json_string)
print(my_data)

#incase of photo do any url in string


    
    
    
    