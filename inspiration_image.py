# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:26:40 2023

@author: Ronaldo
"""

import csv
import os
from random import choice
from datetime import date
from PIL import Image, ImageDraw


source_dir = os.getcwd()


'''
GET DATE AND MAKE HEADER FOR IMAGE
'''

today = date.today()
dateformat = today.strftime("%d/%m/%Y")
datesave = today.strftime("%d-%m")

print(f'\nTodays Date: {dateformat}\n*This is a randomly generated image')

'''
COLLECT NAMES OF ALLAH FROM CSV COMPILE INTO A LIST AND RANDOMLY SELECT ONE
'''

names = []
file_name = r'\names.csv'

# Collect values and append into a list
with open(source_dir+file_name) as read_obj:
    DictReader = csv.DictReader(read_obj)
    for row in DictReader:
        names.append(row)
        
# Return a randomly selected name
name = choice(names)
print()
print(f'Name of Allah: {name["Name"]}\nTranslation: {name["Meaning"]}')


'''
COLLECT GRATITUDE AND AFFIRMATIONS FROM CSV COMPILE INTO A LIST AND RANDOMLY SELECT ONE
'''

gratitudes = []
affirmations = []
file_name = r'\inspire.csv'

# Collect values and append into a list
with open(source_dir+file_name) as read_obj:
    DictReader = csv.DictReader(read_obj)
    for row in DictReader:
        gratitudes.append(row["Gratitude"])
        affirmations.append(row["Affirmation"])

# Return a randomly select gratitude and affirmation
gratitude = choice(gratitudes)
affirmation = choice(affirmations)
print(f'Grateful for: {gratitude}')
print(f'Affirmation of the day: {affirmation}')    


'''
RANDOMLY SELECT IMAGE FROM FOLDER
'''    

image_options = []

for filename in os.listdir(source_dir+"\images"):  # Collect Image Keys
    if filename.endswith(".png"):
        image_options.append(filename)
    else:
        continue
    
image_choice = choice(image_options)
image_title = image_choice.replace('.png', '')

print(f'Photo Title: {image_title}')


'''
SAVE RANDOM IMAGE INTO OUTPUT FOLDER
'''


def draw_logo(image):
    
    LogoIm = Image.open(source_dir+'\images\logo\ResizedLogo.png')
    Logo_Width, Logo_Height = LogoIm.size
    draw.ellipse((15, 935, 145, 1065), ("black"))
    # draw.rectangle((0, image_height-Logo_Height-10, Logo_Width+10, image_height), ("black"))
    image.paste(LogoIm, (9, image_height-124), LogoIm)
    # Save changes.
    image.save(source_dir+'\output\\'+datesave+'.png')

RandomImage = Image.open(source_dir+'\images\\'+str(image_choice))
image_width, image_height = RandomImage.size
draw = ImageDraw.Draw(RandomImage)
draw_logo(RandomImage)
# RandomImage.save(source_dir+'\Output\\'+datesave+'.png')




        