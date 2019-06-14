# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:14:07 2019

@author: user
"""


import pymongo
#import dns # required for connecting with SRV


client = pymongo.MongoClient("mongodb+srv://abhinav:9413731433Ak%40@cluster0-kzorf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

mydb = client.yourdbname

def add_employee(idd, first, last, pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.yourcollectionname.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.yourcollectionname.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()