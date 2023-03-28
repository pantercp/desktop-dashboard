# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:01:50 2023

@author: Ronaldo
"""

import requests

def weather_forecast(city):

   print("\nInitiating Weather API...\n")
   url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
   querystring = {"q":city,"days":"3"}
    
   headers = {
    	"X-RapidAPI-Key": "89a5450d92msh670a1a1da320cd1p1ce2b8jsn907bf0c5798c",
    	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    
   response = requests.request("GET", url, headers=headers, params=querystring)
   print(f'Response Status: {response.status_code}')

   data = response.json()
    
   forecast = data["forecast"]["forecastday"]
   location = data["location"]
   
   print(f'\nWeather Forecast for {data["location"]["name"]}, {data["location"]["country"]}:\n')
       
   for info in forecast:
        print(info["date"])
        print(info["day"]["condition"]["text"])
        print(f'Max: {info["day"]["maxtemp_c"]}°c')
        print(f'Min: {info["day"]["mintemp_c"]}°c')
        print()
    
   return location, forecast

# weather_forecast("Valetta")


