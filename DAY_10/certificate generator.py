# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:21:52 2019

@author: user
"""


"""
Mini Project 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""

from PIL import Image , ImageDraw , ImageFont 
name=input("enter the student name> ")
img = Image.new('RGB', (1000,1000), color = 'black')
img.save('background.png')

img=Image.open('background.png')
print(img.size)
print(img.width)
print(img.height)

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('c:/Windows/Fonts/ARLRDBD.TTF', size=25)
 
(x, y) = (130,50)
message = "CERTIFICATE OF PARTICIPATION IN PYTHON B00TCAMP"
color = 'rgb(255,255,255)' #white color
# draw the message on the background
draw.text((x, y), message, fill=color, font=font)

font1 = ImageFont.truetype('c:/Windows/Fonts/Gabriola.ttf', size=40)
(x,y) = (330,150)
message = "hereby granted to"
color = 'rgb(255,255,255)'
draw.text((x,y),message,fill=color,font=font1)

(x, y) = (330,230)
message = name
color = 'rgb(255,255,255)' #white color
# draw the message on the background
draw.text((x, y), message, fill=color, font=font1)
draw.line((200,280,800,280), fill=(255,255,255), width=2)

(x,y) = (130,320)
message = "for outstanding performance in MACHINE LEARNING"
color = 'rgb(255,255,255)'
draw.text((x,y),message,fill=color,font=font1)

(x, y) = (220,435)
message = "conducted by forsk technologies jaipur"
color = 'rgb(255,255,255)'
draw.text((x, y), message, fill=color, font=font1)


(x, y) = (130,580)
message = "Date : 30 JULY 2019"
color = 'rgb(255,255,255)'
draw.text((x, y), message, fill=color, font=font1)
draw.line((190,620,400,620), fill=(255,255,255), width=2)

(x, y) = (570,580)
message = "Signature"
color = 'rgb(255,255,255)'
draw.text((x, y), message, fill=color, font=font1)
draw.line((700,600,800,600), fill=(255,255,255), width=2)

img.save('new.png')
# Resizing the image 

img1 = Image.open('small_sample1.png')
img1_w, img1_h = img1.size


img2 = Image.open('small_sign.png')
img2_w, img2_h = img2.size

small_im = img1.resize((100,93), resample=Image.BICUBIC)
small_im.save('small_sample1.png')

small_im = img2.resize((120,120), resample=Image.BICUBIC)
small_im.save('small_sign.png')

offset = (400,550)
img.paste(img1,offset)

offset = (700,570)
img.paste(img2,offset)

img.save('new.png')




