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
from weather_api import weather_forecast
from seeking_alpha_api import gme_price
from crypto_api import crypto_prices
from football_api import next_fixture
from insta_api import instagram_info


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
    
    for row in objectives: # Change date format to sort by most recently completed
        row['Deadline'] = datetime.strptime(row['Deadline'], '%d/%m/%Y')
    # Sort by most recent dates
    recent_objectives = sorted(objectives, key=lambda k: k['Deadline'], reverse=False)
    
    y_coord = 605
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.rectangle((1475, y_coord-5, 1915, y_coord + 35), light_clr)
    draw.text((1480, y_coord), "Objectives", dark_clr, font=FontHead)
    y_coord += 40
    
    # This makes sure the for loop runs if iterate num is more than index length
    iterate_num = 7
    if len(recent_objectives) < iterate_num:
        iterate_num = len(recent_objectives)
        
    # Font size for the Objectives
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 18)
    for i in range(iterate_num):
        countdown = objective_countdown(recent_objectives[i]["Deadline"]) # Returns number of days left
        days_width, days_height = get_text_dimensions(f'{countdown} Days', FontObj)
        draw.rectangle((1475, y_coord - 5, 1915, y_coord + 30), test_clr)    
        draw.text((1480, y_coord), f'{recent_objectives[i]["Objective"]}', light_clr, font=FontObj)
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
                milestones.append(row) # Appends all completed objectives
 
    for row in milestones: # Change date format to sort by most recently completed
        row['Complete'] = datetime.strptime(row['Complete'], '%d/%m/%Y').date()
    # Sort by most recent dates
    recent_milestones = sorted(milestones, key=lambda k: k['Complete'], reverse=True)

    y_coord += 20 # Move text coordinates and rectangle down from Objectives
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.rectangle((x_coord - 5, y_coord-5, x_coord + 435, y_coord + 35), light_clr)
    draw.text((x_coord, y_coord), "Milestones", dark_clr, font=FontHead)
    y_coord += 40 # Move y coord down from heading
    
    # Font size for the Objectives
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    for i in range(3):
        obj_width, obj_height = get_text_dimensions(recent_milestones[i]["Objective"], FontObj)
        draw.rectangle((x_coord - 5, y_coord - 5, 1915, y_coord + 30), test_clr)
        draw.text((x_coord, y_coord), recent_milestones[i]["Objective"], light_clr, font=FontObj)
        y_coord += 30

    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    return y_coord


'''
DRAW PRAYER TIMES FOR CURRENT DAY ONTO WALLPAPER
'''

def draw_prayertimes(x_coord, y_coord):

    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 25)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 200, y_coord + 30), light_clr)
    draw.rectangle((x_coord - 5, y_coord + 30, x_coord + 200, y_coord + 215), test_clr)
    draw.text((x_coord + 15, y_coord), "Prayer Times", dark_clr, font=FontHead)
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

    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 240, y_coord + 50), test_clr)
    draw.text((x_coord, y_coord), f'Date: {hijri["day"]} {hijri["month"]["en"]} \
{hijri["year"]}{hijri["designation"]["abbreviated"]}\nWeekday: {hijri["weekday"]["en"]}'\
, light_clr, font=FontHead)
        
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
'''
DRAW 3-DAY WEATHER FORECAST ONTO WALLPAPER
'''

def draw_forecast(x_coord, y_coord):
    
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 435, y_coord + 30), light_clr)
    draw.rectangle((x_coord - 5, y_coord + 30, x_coord + 435, y_coord + 130), test_clr)
    draw.text((x_coord, y_coord), f'Weather Forecast for {location["name"]}, \
{location["country"]}', dark_clr, font=FontHead)
    y_coord += 10
    FontObj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 19)
    
    for info in forecast:
         draw.text((x_coord, y_coord + 30),f'{info["date"]}\n{info["day"]["condition"]["text"][0:14]}\
\nMax: {info["day"]["maxtemp_c"]}°c\nMin: {info["day"]["mintemp_c"]}°c', light_clr, font=FontObj)
         x_coord += 150
    
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    

'''
DRAW GAMESTOP PRICE ONTO WALLPAPER
'''

def draw_market(x_coord, y_coord):
    
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
    FontBody = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 18)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 130, y_coord + 30), light_clr)
    draw.rectangle((x_coord - 5, y_coord + 30, x_coord + 130, y_coord + 100), test_clr)
    draw.text((x_coord + 30, y_coord), 'Market', dark_clr, font=FontHead)
    y_coord += 35
    draw.text((x_coord + 10, y_coord), f'{symbol}: ${price}\nBTC: ${btc}\nETH: ${eth}', light_clr, font=FontBody)
    y_coord += 35
    
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
    
'''
DRAW SHEFFIELD UNITED FIXTURE DETAILS
'''

def draw_fixtures(x_coord, y_coord):
    
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
    FontBody = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 18)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 130, y_coord + 30), light_clr)
    draw.rectangle((x_coord - 5, y_coord + 30, x_coord + 130, y_coord + 100), test_clr)
    draw.text((x_coord + 7, y_coord), 'The Blades', dark_clr, font=FontHead)
    y_coord += 35
    draw.text((x_coord, y_coord), f'  {opponent["date"]}\n {opponent["name"][0:12]} ({opponent["venue"][0]})\
\n      {opponent["form"]}', light_clr, font=FontBody)
    y_coord += 35
    
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    

'''
DRAW BUDGET BACKPACKERS IG STATS
'''

def draw_instagram(x_coord, y_coord):
    
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
    FontBody = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 200, y_coord + 30), light_clr)
    draw.rectangle((x_coord - 5, y_coord + 30, x_coord + 200, y_coord + 85), test_clr)
    draw.text((x_coord, y_coord), instagram["account"], dark_clr, font=FontHead)
    y_coord += 35
    draw.text((x_coord + 25, y_coord), f' Following: {instagram["following"]}\
\nFollowers: {instagram["followers"]}', light_clr, font=FontBody)
    
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    

'''
DRAW DASHBOARD TITLES
'''

def draw_titles(x_coord_1, y_coord_1, x_coord_2, y_coord_2):
    
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
    draw.rectangle((x_coord_1 - 5, y_coord_1 - 5, x_coord_1 + 300, y_coord_1 + 35), test_clr)
    draw.rectangle((x_coord_2 - 5, y_coord_2 -5, x_coord_2 + 335, y_coord_2 + 35), test_clr)
    draw.text((x_coord_1, y_coord_1 - 2), "Personal Dashboard", light_clr, font=FontHead)
    draw.text((x_coord_2, y_coord_2 - 2), "Productivity Dashboard", light_clr, font=FontHead)
    
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
    
'''
DISPLAY UPCOMING BIRTHDAY
'''

def birthday_countdown():

    DictDates = []
    Upcoming_Dates = []
    
    with open(source_dir+r'\birthdays.csv', 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if len(row["Birthday"]) == 10: # Filter out dates with missing info            
                row["Birthdate"] = row["Birthday"][0:6] + str(today.year) # Get birthdate for year
                row["Birthdate"] = datetime.strptime(row["Birthdate"], '%d/%m/%Y') # Make into date time object  
                row["Birthday"] = datetime.strptime(row["Birthday"], '%d/%m/%Y') # Make into date time object 
                row["Countdown"] = objective_countdown(row["Birthdate"]) # Use timedelta function for time diff
                row["Turns"] = today.year - row["Birthday"].year
                DictDates.append(row)
              
        # Sort Birthdates by order throughout the year        
        Sorted = sorted(DictDates, key = lambda item: item['Countdown'], reverse = False)
        
        print("\nUpcoming Birthdays:\n")
        i = 0
        for row in Sorted: # Print next 5 upcoming birthdays
            if row["Countdown"] > 0 and i < 5:
                print(f'{row["Name"]} turns {today.year - row["Birthday"].year}\
 in {row["Countdown"]} days [{row["Birthday"].strftime("%d/%m/%y")}]')
                Upcoming_Dates.append(row)
                i += 1

    return Upcoming_Dates
    

'''
DRAW CELEBRATION NOTIFICATIONS
'''

def draw_celebration(x_coord, y_coord):
    
    FontHead = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 24)
    FontBody = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
    draw.rectangle((x_coord - 5, y_coord - 5, x_coord + 150, y_coord + 30), light_clr)
    draw.rectangle((x_coord - 5, y_coord + 30, x_coord + 150, y_coord + 85), test_clr)
    draw.text((x_coord, y_coord), "Celebration", dark_clr, font=FontHead)
    y_coord += 35
    draw.text((x_coord, y_coord), f'{Upcoming_Dates[0]["Name"]} turns {Upcoming_Dates[0]["Turns"]}\
\n     in {Upcoming_Dates[0]["Countdown"]} days!', light_clr, font=FontBody)
    
    DesktopImage.save(source_dir+r'\output\wallpaper.png')
  

'''
PROGRAM RUNS FROM HERE
'''

source_dir = "C:\\Users\\Ronaldo\\OneDrive\\Python\\git\\ninetynine"
today = date.today()
datesave = today.strftime("%d-%m")
file_name = r'\objectives.csv'
DesktopImage = Image.open(source_dir+r'\background\template.png')
draw = ImageDraw.Draw(DesktopImage)
# Paste inspiration image on wallpaper
inspire_wallpaper()
# Preselect Fonnt and Colors
fontsFolder = 'C:\Windows\Fonts'
dark_clr, light_clr, test_clr = (23, 42, 58), (105, 209, 197), (12, 21, 29)
# Draws Objectives onto wallpaper and returns y for milestones
y_coord = draw_objectives()
# Draws Milestones below the objectives
y_coord = draw_milestones(1480, y_coord)
# Gathers prayer times for the day
timings, hijri = prayer_api.prayer_timings()
# Removes unneeded timings from dictionary
timings.pop("Imsak"),timings.pop("Lastthird"),timings.pop("Firstthird"),
timings.pop("Sunset"),timings.pop("Midnight")
# Draws the prayer times & hijri date on the desktop wallpaper
draw_prayertimes(1500, 205)
draw_hijri(5,5)
# Get the weather forecast by City
location, forecast = weather_forecast("London")
draw_forecast(1480, 60)
# Get market prices for interested holdings
symbol, price = gme_price()
btc, eth = crypto_prices()
draw_market(1750, 205)
# Get next fixture details for SUFC
opponent = next_fixture()
draw_fixtures(1750, 320)
# Get instagram details
instagram = instagram_info("budget.backpackers")
draw_instagram(1500, 450)
# Draw Personal/Productivity Dashboard
draw_titles(1555, 10, 1535, 555)
Upcoming_Dates = birthday_countdown()
draw_celebration(1750, 450)
            
