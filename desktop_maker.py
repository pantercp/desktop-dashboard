# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:26:44 2022

@author: Ronaldo
"""

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date
import csv
import prayer_api


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
    draw.rectangle((1475, y_coord-5, 1915, y_coord + 35), test_clr)
    draw.text((1480, y_coord), "Objectives", light_clr, font=FontHead)
    y_coord += 35
    # Font size for the Objectives
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 18)
    for row in objectives:
        deadline = row["Deadline"] # Get due date for objective
        deadlineFormat = datetime.strptime(deadline, "%d/%m/%Y") # Format for function
        countdown = objective_countdown(deadlineFormat) # Returns number of days left
        # Draws objectives and deadline countdown onto wallpaper image
        obj_width, obj_height = get_text_dimensions(f'{row["Objective"]}', FontObj)
        days_width, days_height = get_text_dimensions(f'{countdown} Days', FontObj)
        draw.rectangle((1475, y_coord, 1915, y_coord + 30), test_clr)    
        draw.text((1480, y_coord), f'{row["Objective"]}', light_clr, font=FontObj)
        draw.text((1910 - days_width, y_coord), f'{countdown} Days', light_clr, font=FontObj)
        y_coord += 30 # Moves coordinate for next objective to be written

    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    return y_coord # So that the milestones can be drawn below the objectives


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

def draw_milestones(x_coord, y_coord):

    milestones = []
    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] != 'FALSE':
                milestones.append(row)
    
    y_coord += 20
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.rectangle((x_coord - 5, y_coord-5, x_coord + 440, y_coord + 35), test_clr)
    draw.text((x_coord, y_coord), "Milestones", light_clr, font=FontHead)
    y_coord += 35
    
    # Font size for the Objectives
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    for row in milestones:
        obj_width, obj_height = get_text_dimensions(row["Objective"], FontObj)
        draw.rectangle((x_coord - 5, y_coord, 1915, y_coord + 30), test_clr)
        draw.text((x_coord, y_coord), row["Objective"], light_clr, font=FontObj)
        y_coord += 30

    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    return y_coord


'''
DRAW PRAYER TIMES FOR CURRENT DAY ONTO WALLPAPER
'''

def draw_prayertimes(x_coord, y_coord):

    y_coord += 20
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 200, y_coord + 215), test_clr)
    draw.text((x_coord, y_coord), "Prayer Times", light_clr, font=FontHead)
    y_coord += 35
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)

    for info in timings:
        obj_width, obj_height = get_text_dimensions(f'{info} {timings[info]}', FontObj)
        draw.text((x_coord, y_coord),f'{info} {timings[info]}', light_clr, font=FontObj)
        y_coord += 30
        print(info, timings[info])
        
    DesktopImage.save(source_dir+r'\output\wallpaper.png')

'''
DRAW PRAYER TIMES FOR CURRENT DAY ONTO WALLPAPER
'''

def draw_hijri(x_coord, y_coord):

    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 200, y_coord + 80), test_clr)
    draw.text((x_coord, y_coord), f'{hijri["day"]} {hijri["month"]["en"]} {hijri["year"]}', light_clr, font=FontHead)
        
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    
'''
PROGRAM RUNS FROM HERE
'''

source_dir = "C:\\Users\\Ronaldo\\OneDrive\\Python\\git\\ninetynine"
today = date.today()
datesave = today.strftime("%d-%m")

DesktopImage = Image.open(source_dir+r'\background\template.png')
draw = ImageDraw.Draw(DesktopImage)

inspire_wallpaper()

file_name = r'\objectives.csv'
fontsFolder = 'C:\Windows\Fonts'
dark_clr, light_clr = (23, 42, 58), (105, 209, 197)
test_clr = (12, 21, 29)
# Draws Objectives onto wallpaper and returns y for milestones
y_coord = draw_objectives()
# Draws Milestones below the objectives
y_coord = draw_milestones(1480, y_coord)
# Gathers prayer times for the day
timings, hijri = prayer_api.prayer_timings()
timings.pop("Imsak"),timings.pop("Lastthird"),timings.pop("Firstthird"),
timings.pop("Sunset"),timings.pop("Midnight")   
draw_prayertimes(1600, y_coord)


draw_hijri(1600,800)
