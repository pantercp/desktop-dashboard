# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:26:40 2023

@author: Ronaldo
"""

import csv
import os
from random import choice
from datetime import date
from PIL import Image, ImageDraw, ImageFont


'''
FUNCTION TO DRAW LOGO IN CORNER OF RANDOMLY SELECTED IMAGE
'''
def draw_logo(image):
    
    image_width, image_height = image.size
    
    LogoIm = Image.open(source_dir+'\images\logo\ResizedLogo.png')
    Logo_Width, Logo_Height = LogoIm.size
    draw.ellipse((15, 935, 145, 1065), ("black"))
    # draw.rectangle((0, image_height-Logo_Height-10, Logo_Width+10, image_height), ("black"))
    image.paste(LogoIm, (9, image_height-124), LogoIm)
    # Save changes.
    image.save(source_dir+'\output\\'+datesave+'.png')

'''
GETS TEXT DIMENSIONS FROM CHOSEN STING AND FONT
'''
def get_text_dimensions(text_string, font):

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

'''
DRAW HEADER IN TOP LEFT CORNER OF IMAGE
'''

def draw_header(image):

    head, subhead, disc = "Daily Positivity Generator", "Todays Date: "+dateformat,\
        "*This is a randomly generated image"

    FontProj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
    FontDate = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 19)
    FontDisc = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 14)
    # Dimensions for date and info box
    proj_width, proj_height = get_text_dimensions(head, FontProj)
    date_width, date_height = get_text_dimensions(subhead, FontDate)
    disc_width, disc_height = get_text_dimensions(disc, FontDisc)
    
    # Draw background for date and info box
    draw.rectangle((0, 0, proj_width+10, proj_height+date_height+5), dark_clr)
    draw.rectangle((0, proj_height+date_height+5, proj_width+10,
                   proj_height+date_height+disc_height+5), light_clr)
    
    # Draw text for date and info box
    draw.text((5, 5), head, light_clr, font=FontProj)
    draw.text((5, 5+proj_height), subhead, light_clr, font=FontDate)
    draw.text((5, 5+proj_height+date_height), disc, dark_clr, font=FontDisc)
    
    image.save(source_dir+'\output\\'+datesave+'.png')

'''
COLLECT NAMES OF ALLAH FROM CSV COMPILE INTO A LIST AND RANDOMLY SELECT ONE
'''

def choose_name():
    
    names = []
    file_name = r'\names.csv'

    # Collect values and append into a list
    with open(source_dir+file_name) as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            names.append(row)
            
    # Return a randomly selected name
    name = choice(names)
    return name

'''
COLLECT GRATITUDE AND AFFIRMATIONS FROM CSV RANDOMLY SELECT ONE OF EACH
'''

def choose_insp():
    
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
    
    return gratitude, affirmation

'''
RANDOMLY SELECT IMAGE FROM FOLDER
'''    

def choose_image():
        
    image_options = []
    
    for filename in os.listdir(source_dir+"\images"):  # Collect Image Keys
        if filename.endswith(".png"):
            image_options.append(filename)
        else:
            continue
        
    image_choice = choice(image_options)
    return image_choice
    
'''
PROGRAM RUNS FROM HERE
'''

source_dir = os.getcwd()
today = date.today()
dateformat = today.strftime("%d/%m/%Y")
datesave = today.strftime("%d-%m")
# Return a random name of God
name = choose_name()
# Return inspiration variables
gratitude, affirmation = choose_insp()
# Choose inspiration image
image_choice = choose_image()

# Display all randomly selected variables
print(f'\nTodays Date: {dateformat}\n*This is a randomly generated image')
print(f'\nAffirmation of the day: {affirmation}')
print(f'Name of Allah: {name["Name"]}\nTranslation: {name["Meaning"]}')
print(f'Photo Title: {image_choice.replace(".png", "")}')
print(f'Grateful for: {gratitude}')

# Opens the inspiration image
RandomImage = Image.open(source_dir+'\images\\'+str(image_choice))
# Ability to draw on inspiration image
draw = ImageDraw.Draw(RandomImage)
# Puts CJPixel logo in bottom left corner
draw_logo(RandomImage)
# Locate & choose font format for drawing text
fontsFolder = 'C:\Windows\Fonts'
# Variables for colours
dark_clr, light_clr = (23, 42, 58), (105, 209, 197)
# Creates header in top left corner
draw_header(RandomImage)


'''
REQUIRED FUNCTIONS
'''

# DRAW INSPIRATION TEXT
