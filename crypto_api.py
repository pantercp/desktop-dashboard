# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:38:12 2023

@author: Ronaldo
"""

'''
Bitcoin USD Pair ID = 945629
Ethereum USD Pair ID = 997650
'''

import requests
import re


def crypto_prices():

    print("Initiating API for crypto prices...\n")
    
    url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/list-pairs"
    
    querystring = {"time_utc_offset":"28800","lang_ID":"1"}
    
    headers = {
    	"X-RapidAPI-Key": "89a5450d92msh670a1a1da320cd1p1ce2b8jsn907bf0c5798c",
    	"X-RapidAPI-Host": "investing-cryptocurrency-markets.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(f'Response Status: {response.status_code}\n')
    data = response.json()
    
    pairs_data = data["data"][0]["screen_data"]["pairs_data"]
    
    btc_id = 945629
    eth_id = 997650
    
    for pairs in pairs_data:
        if pairs["pair_ID"] == btc_id:
            btc_price_string = pairs["last"]
            btc_price_string_1 = re.sub(",", "", btc_price_string)
            btc_price = int(float(btc_price_string_1))
            
        elif pairs["pair_ID"] == eth_id:
            eth_price_string = pairs["last"]
            eth_price_string_1 = re.sub(",", "", eth_price_string)
            eth_price = int(float(eth_price_string_1))
            
    print(f'Latest Market Prices:\nBTC: ${btc_price}\nETH: ${eth_price}\n')
            
    return btc_price, eth_price
 
        