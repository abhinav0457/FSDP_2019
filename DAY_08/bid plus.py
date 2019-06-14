# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:16:37 2019

@author: user
"""


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
#pip install selenium


import pandas as pd
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/user/Downloads/chromedriver.exe")

url = "https://bidplus.gem.gov.in/bidlists"

driver.get(url)

bidn0=[]
items=[]
quantity=[]
department=[]
start=[]
end=[]

for i in range(1,11):
    get_result = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    bidn0.append(get_result.text)
    get_result.click()

for i in range(1,11):
    a=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    items.append(a)
    b=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    department.append(b)
    c=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    start.append(c)
    d=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    end.append(d)
    e=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]').text
    quantity.append(e)


import pandas as pd
from collections import OrderedDict

col_name = ["BID NO","Items","Quantity","Department Name And Address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[bidn0,items,quantity,department,start,end]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")


driver.quit()

