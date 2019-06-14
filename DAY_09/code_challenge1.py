# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:31:21 2019

@author: user
"""


"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
import sqlite3
from pandas import DataFrame

conn=sqlite3.connect('db_university.db')

c=conn.cursor()

c.execute(""" CREATE TABLE students(student_name TEXT,
                                    student_age INTEGER,
                                    student_roll_no INTEGER,
                                    student_branch TEXT)"""
         )
conn.commit()

c.execute("INSERT INTO students VALUES('abhi',19,1,'cs')")
c.execute("INSERT INTO students VALUES('ram',20,2,'ce')")
c.execute("INSERT INTO students VALUES('shyam',19,3,'it')")
c.execute("INSERT INTO students VALUES('mohan',21,4,'ece')")
c.execute("INSERT INTO students VALUES('sohan',19,5,'ee')")
c.execute("INSERT INTO students VALUES('john',29,9,'cs')")
c.execute("INSERT INTO students VALUES('mayur',19,8,'it')")
c.execute("INSERT INTO students VALUES('abhimanyu',19,7,'cs')")
c.execute("INSERT INTO students VALUES('abhishek',19,4,'cs')")
c.execute("INSERT INTO students VALUES('ankit',19,13,'cs')")
conn.commit()

c.execute("SELECT *FROM students")


df = DataFrame(c.fetchall())  
df.columns = ["student_name","student_age","student_roll_no","student_branch"]
conn.commit()
conn.close()