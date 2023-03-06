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
DRAW INSPIRATIONAL TEXT IN BOTTOM RIGHT OF RANDOM IMAGE
'''

def inspire_text(image):
    
    # Choose font type and size
    FontOne = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 23)
    FontTwo = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    
    # Get text width and heights
    grat_width, grat_height = get_text_dimensions("Something to be grateful for: "+gratitude, FontOne)
    title_width, title_height = get_text_dimensions("Photo: "+image_choice.replace(".png", ""), FontTwo)
    tran_width, tran_height = get_text_dimensions("Translation: "+name["Meaning"], FontTwo)
    name_width, name_height = get_text_dimensions("Names of Allah: "+name["Name"], FontOne)
    affirm_width, affirm_height = get_text_dimensions(affirmation, FontOne)
    
    # Make widest text the width for the blurbs background
    textWidths = [grat_width, tran_width, name_width, title_width, affirm_width]
    blurb_width = max(textWidths)
    
    # Make background for the blurb the total height of all text
    blurb_height = grat_height + tran_height + name_height + title_height

    padding = 10
    # Draw backgrounds for the blurb
    draw.rectangle((image_width-blurb_width-padding, image_height-blurb_height-padding/2,
                    image_width+blurb_width, image_height+blurb_height), light_clr)
    draw.rectangle((image_width-blurb_width-padding, image_height-blurb_height-affirm_height
                , image_width+blurb_width, image_height-blurb_height), dark_clr)

    
    # Drawing Text for the blurb
    draw.text((image_width-blurb_width-padding/2, image_height-grat_height),
              "Something to be grateful for: "+gratitude, dark_clr, font=FontOne)
    draw.text((image_width-blurb_width-padding/2, image_height-grat_height-tran_height),
              "Photo: "+image_choice.replace(".png", ""), dark_clr, font=FontTwo)
    draw.text((image_width-blurb_width-padding/2, image_height-grat_height-tran_height-name_height),
              "Translation: "+name["Meaning"], dark_clr, font=FontTwo)
    draw.text((image_width-blurb_width-padding/2, image_height-blurb_height),
              "Names of Allah: "+name["Name"], dark_clr, font=FontOne)
    
    # Drawing Text for the header of the blurb
    affirm_xcoord = image_width-(((blurb_width+10)/2)+(affirm_width/2))
    draw.text((affirm_xcoord, image_height-blurb_height-affirm_height),
              affirmation, light_clr, font=FontOne)
    
    image.save(source_dir+'\output\\'+datesave+'.png')


'''
PROGRAM RUNS FROM HERE
'''

source_dir = "C:\\Users\\Ronaldo\\OneDrive\\Python\\git\\ninetynine"
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
print(f'\nTodays Date: {dateformat}')
print(f'\nAffirmation of the day: {affirmation}')
print(f'Name of Allah: {name["Name"]}\nTranslation: {name["Meaning"]}')
print(f'Photo Title: {image_choice.replace(".png", "")}')
print(f'Grateful for: {gratitude}')

# Opens the inspiration image
RandomImage = Image.open(source_dir+'\images\\'+str(image_choice))
# Ability to draw on inspiration image
draw = ImageDraw.Draw(RandomImage)
# Inspiration image sizes
image_width, image_height = RandomImage.size
# Puts CJPixel logo in bottom left corner
draw_logo(RandomImage)
# Locate & choose font format for drawing text
fontsFolder = 'C:\Windows\Fonts'
# Variables for colours
dark_clr, light_clr = (23, 42, 58), (105, 209, 197)
# Creates header in top left corner
draw_header(RandomImage)
# Draw inspiration text
inspire_text(RandomImage)

print("\nContinuing to Desktop Maker...")


