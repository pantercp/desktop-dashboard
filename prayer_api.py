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
    
    response = requests.get(f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city=London&country=United Kingdom&method=1')
    print(f'Response Status: {response.status_code}\n')
    
    data = response.json()
    
    # Print all the dates within data
    for info in data["data"]:
        if dateformat in info["date"]["gregorian"]["date"]:
            timings = info["timings"]
    
    # for info in timings:
    #     print(info, timings[info])
        
    return timings
        
    










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



