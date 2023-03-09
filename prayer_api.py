# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:23:13 2023

@author: Ronaldo
"""

import requests
from datetime import date


def prayer_timings():

    # Intro info to user for api
    print("\nInitiating Aladhan Prayer Times API\n")
    # Get correct date and location for the api request
    today = date.today()
    dateformat = today.strftime("%d-%m-%Y")
    month = today.strftime("%m")
    year = today.strftime("%Y")
    city = "London"
    country = "United Kingdom"
    # Confirm to user date and location for prayer times
    print(f'Getting Prayer Times for {dateformat} in {city}, {country}...\n ')
    # Submit api request with desired details
    response = requests.get(f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={city}&country={country}&method=1')
    print(f'Response Status: {response.status_code}\n')
    # Convert response object from json
    data = response.json()
    
    # Print all the dates within data
    for info in data["data"]:
        if dateformat in info["date"]["gregorian"]["date"]:
            timings = info["timings"]
            hijri = info["date"]["hijri"]
    
        
    return timings, hijri
        
    

