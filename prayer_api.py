# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:23:13 2023

@author: Ronaldo
"""

import requests
from datetime import date


def prayer_timings():

    print("\nInitiating Aladhan Prayer Times API\n")
    
    today = date.today()
    dateformat = today.strftime("%d-%m-%Y")
    month = today.strftime("%m")
    year = today.strftime("%Y")
    city = "London"
    country = "United Kingdom"
    
    print(f'Getting Prayer Times for {dateformat} in {city}, {country}...\n ')
    
    response = requests.get(f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={city}&country={country}&method=1')
    print(f'Response Status: {response.status_code}\n')
    
    data = response.json()
    
    # Print all the dates within data
    for info in data["data"]:
        if dateformat in info["date"]["gregorian"]["date"]:
            timings = info["timings"]
            hijri = info["date"]["hijri"]
    
    # for info in timings:
    #     print(info, timings[info])
        
    return timings, hijri
        
    
# timings, hijri = prayer_timings()

# print(hijri["day"], hijri["month"]["en"], hijri["year"],"AH")
# print("Weekday:", hijri["weekday"]["en"])








# import requests
# from datetime import date


# print("\nInitiating Aladhan Prayer Times API\n")

# today = date.today()
# dateformat = today.strftime("%d-%m-%Y")
# month = today.strftime("%m")
# year = today.strftime("%Y")

# response = requests.get(f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city=London&country=United Kingdom&method=1')
# print(f'Response Status: {response.status_code}\n')

# data = response.json()

# # Print all the dates within data
# for info in data["data"]:
#     if dateformat in info["date"]["gregorian"]["date"]:
#         timings = info["timings"]

# for info in timings:
#     print(info, timings[info])



