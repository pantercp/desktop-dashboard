# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:15:48 2023

@author: Ronaldo
"""

'''
GME: 1290
S&P: 587766
'''

import requests

def gme_price():
    
    print("Initiating API for market prices...\n")


    url = "https://seeking-alpha.p.rapidapi.com/market/get-realtime-quotes"
    
    querystring = {"sa_ids":"1290"}
    
    headers = {
     	"X-RapidAPI-Key": "89a5450d92msh670a1a1da320cd1p1ce2b8jsn907bf0c5798c",
     	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(f'Response Status: {response.status_code}\n')

    data = response.json()
    
    symbol = data["real_time_quotes"][0]["symbol"]
    price = data["real_time_quotes"][0]["last"]

    print(f'Latest Market Prices:\n{symbol}: ${price}\n')


    return symbol, price
