# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:26:44 2022

@author: Ronaldo
"""

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date
import csv


'''
PASTES THE INSPIRATION IMAGE ONTO THE DESTOP WALLPAPER TEMPLATE
'''

def inspire_wallpaper():
    
    # Opens the template wallpaper and preps for drawing
    Desktop_Width, Desktop_Height = DesktopImage.size
    
    # Changes inspiration image from 1080sq to 1020sq
    OriginalInsp = Image.open(source_dir+'\output\\'+datesave+'.png')
    original_width, original_height = OriginalInsp.size
    FittedInsp = OriginalInsp.resize(
        (int(original_width - 60), int(original_height - 60)))
    
    # Pastes inspiration image onto centre of wallpaper
    Fitted_Width, Fitted_Height = FittedInsp.size
    DesktopImage.paste(
            FittedInsp, ((Desktop_Width//2)-(Fitted_Width//2), (0)))
    DesktopImage.save(source_dir+r'\output\wallpaper.png')

'''
GETS SIZE OF FONTING FOR TOTAL STRING OF TEXT
'''

def get_text_dimensions(text_string, font):

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

'''
DISPLAY OUTSTANDING OBJECTIVES
'''

def draw_objectives():

    objectives = []
    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] == 'FALSE':
                objectives.append(row)
    
    y_coord = 20
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.text((1475, y_coord), "Objectives", light_clr, font=FontHead)
    y_coord += 35
    # Font size for the Objectives
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    for row in objectives:
        deadline = row["Deadline"]
        deadlineFormat = datetime.strptime(deadline, "%d/%m/%Y")
        countdown = objective_countdown(deadlineFormat)
        obj_width, obj_height = get_text_dimensions(row["Objective"]+str(countdown)+"Days", FontObj)
        draw.text((1475, y_coord), f'{row["Objective"]} {countdown} Days', light_clr, font=FontObj)
        y_coord += 30

    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    return y_coord


'''
FIND NUMBER OF DAYS LEFT TO COMPLETE OBJECTIVE
'''

def objective_countdown(date):
    
    my_datetime = datetime.combine(today, datetime.min.time())
    diff = date - my_datetime
    countdown = diff.days
    
    return countdown
    

'''
DISPLAY OUTSTANDING OBJECTIVES
'''

def draw_milestones(y_coord):

    milestones = []
    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] != 'FALSE':
                milestones.append(row)
    
    y_coord += 10
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.text((1475, y_coord), "Milestones", light_clr, font=FontHead)
    y_coord += 35
    
    # Font size for the Objectives
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    for row in milestones:
        obj_width, obj_height = get_text_dimensions(row["Objective"], FontObj)
        draw.text((1475, y_coord), row["Objective"], light_clr, font=FontObj)
        y_coord += 30

    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    return y_coord


source_dir = os.getcwd()
today = date.today()
datesave = today.strftime("%d-%m")

DesktopImage = Image.open(source_dir+r'\background\template.png')
draw = ImageDraw.Draw(DesktopImage)

inspire_wallpaper()

file_name = r'\objectives.csv'
fontsFolder = 'C:\Windows\Fonts'
dark_clr, light_clr = (23, 42, 58), (105, 209, 197)
# Draws Objectives onto wallpaper and returns y for milestones
y_coord = draw_objectives()
# Draws Milestones below the objectives
draw_milestones(y_coord)



