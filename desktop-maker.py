# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:26:44 2022

@author: Ronaldo
"""

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import date
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

def collect_objectives():

    objectives = []
    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] == 'FALSE' and row not in objectives:
                objectives.append(row)
    
    for row in objectives:
        print(row["Objective"],row["Deadline"])

    # Font size for the Objectives
    FontObj = ImageFont.truetype(
    os.path.join(fontsFolder, 'arial.ttf'), 25)
    
    # Draw the objectives on the background
    obj_width, obj_height = get_text_dimensions(objectives[0]["Objective"], FontObj)
    draw.text((1500-(obj_width/2), 555), objectives[0]["Objective"],
                  light_clr, font=FontObj)

    DesktopImage.save(source_dir+r'\output\wallpaper.png')


source_dir = os.getcwd()
today = date.today()
datesave = today.strftime("%d-%m")

DesktopImage = Image.open(source_dir+r'\background\template.png')
draw = ImageDraw.Draw(DesktopImage)

inspire_wallpaper()

file_name = r'\objectives.csv'
fontsFolder = 'C:\Windows\Fonts'
dark_clr, light_clr = (23, 42, 58), (105, 209, 197)
collect_objectives()




'''
CHANGE WALLPAPER TO IMAGE FOUND IN BACKGROUND DIRECTORY

import os
import productivity
import inspiration_image
import struct
import ctypes


source_dir = os.getcwd()



SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = (source_dir+r'\background\output.png')


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA

def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())


# change_wallpaper()
'''