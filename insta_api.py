# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:34:06 2023

@author: Ronaldo
"""

import requests

def instagram_info(account):

    print(f'Initiating Instagram for {account} info...\n')

    url = "https://instagram28.p.rapidapi.com/user_info"
    
    querystring = {"user_name":account}
    
    headers = {
    	"X-RapidAPI-Key": "89a5450d92msh670a1a1da320cd1p1ce2b8jsn907bf0c5798c",
    	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(f'Response Status: {response.status_code}\n')

    data = response.json()
    
    account = data["data"]["user"]
    posts = data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
    followers = account["edge_followed_by"]["count"]
    following = account["edge_follow"]["count"]
    
    likes = 0
    for post in posts:
        likes += post["node"]["edge_liked_by"]["count"]
    
    
    print(f'Account: {account["ads_page_name"]}\nFollowers: {followers}\nFollowing: {following}\n\
Last 12 Posts: {likes} Likes')
    
    instagram = {"account": account["ads_page_name"], "followers": followers, "following": following, "likes": likes}
    
    return instagram


# instagram = instagram_info("budget.backpackers")
    




