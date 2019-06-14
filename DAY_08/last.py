# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:41:25 2019

@author: user
"""


     

"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/user/Downloads/chromedriver.exe")
url='http://forsk.in/images/Forsk_logo_bw.png'

driver.get(url)
get_result = driver.find_element_by_xpath('/html/body/img')
get_result.click() 



