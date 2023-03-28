# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:37:47 2023

@author: Ronaldo
"""

'''
Championship ID: 40
Sheffield United ID: 62
Bramall Lane: 581
'''

import requests
from datetime import date, datetime


'''
RETURN TEAMS LAST FIVE RESULTS
'''

def get_form(team_id):
    
    print("Gathering Opponents Data...\n")

    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
    
    querystring = {"league":"40","season":"2022","team":team_id}
    
    headers = {
    	"X-RapidAPI-Key": "89a5450d92msh670a1a1da320cd1p1ce2b8jsn907bf0c5798c",
    	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(f'Response Status: {response.status_code}\n')

    data = response.json()
    
    form = data["response"]["form"][-5::]
    print(f'Opponents Last Five Results:\n{form}')

    return form


'''
FIXTURES BY TEAM ID
'''

def next_fixture():

    print("Initiating Football API...\n")

    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    
    querystring = {"season":"2022","team":"62"}
    
    headers = {
    	"X-RapidAPI-Key": "89a5450d92msh670a1a1da320cd1p1ce2b8jsn907bf0c5798c",
    	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = response.json()
    
    print(f'Response Status: {response.status_code}')
    
    fixtures = data["response"]
    remaining_fixtures = []
    
    for fixture in fixtures:
        date_str = fixture["fixture"]["date"][:10]
        date = datetime.strptime(date_str, "%Y-%m-%d")
        diff = date - my_datetime
        countdown = diff.days
        if countdown >= 0:
            remaining_fixtures.append(fixture)
    
    for row in remaining_fixtures: # Change date format to sort by most recently completed
        row["fixture"]["date"] = datetime.strptime(row["fixture"]["date"][:10], '%Y-%m-%d').date()
    # Sort by upcoming dates
    remaining_fixtures = sorted(remaining_fixtures, key=lambda k: k["fixture"]["date"], reverse=False)
    
    print('\nThe next fixture for Sheffield United is:\n')
    print(f'{remaining_fixtures[0]["fixture"]["date"]}')
    
    if remaining_fixtures[0]["teams"]["home"]["name"] != "Sheffield Utd":
        print(f'{remaining_fixtures[0]["teams"]["home"]["name"]}\nAway')
        print(f'Team ID: {remaining_fixtures[0]["teams"]["home"]["id"]}\n')
        opponent = {"name": remaining_fixtures[0]["teams"]["home"]["name"],\
                    "id": remaining_fixtures[0]["teams"]["home"]["id"],\
                        "venue": "Away", "date": remaining_fixtures[0]["fixture"]["date"]} 
        
    elif remaining_fixtures[0]["teams"]["away"]["name"] != "Sheffield Utd":
        print(f'{remaining_fixtures[0]["teams"]["away"]["name"]}\nHome')
        print(f'Team ID: {remaining_fixtures[0]["teams"]["away"]["id"]}\n')
        opponent = {"name": remaining_fixtures[0]["teams"]["away"]["name"],\
                    "id": remaining_fixtures[0]["teams"]["away"]["id"],\
                        "venue": "Home", "date": remaining_fixtures[0]["fixture"]["date"]}
        
    form = get_form(opponent["id"])
    opponent["form"] = form
    
    return opponent


'''
PROGRAM RUNS FROM HERE
'''

today = date.today()
my_datetime = datetime.combine(today, datetime.min.time())



