# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:26:40 2023

@author: Ronaldo
"""

import csv
import os
from random import choice


source_dir = os.getcwd()




'''
COLLECT NAMES OF ALLAH FROM CSV COMPILE INTO A LIST AND RANDOMLY SELECT ONE
'''

names = []
file_name = r'\names.csv'

# Collect values and append into a list
with open(source_dir+file_name) as read_obj:
    DictReader = csv.DictReader(read_obj)
    for row in DictReader:
        names.append(row)
        
# Return a randomly selected name
name = choice(names)
print()
print(f'Name of Allah: {name["Name"]}\nTranslation: {name["Meaning"]}')


'''
COLLECT GRATITUDE AND AFFIRMATIONS FROM CSV COMPILE INTO A LIST AND RANDOMLY SELECT ONE
'''

gratitudes = []
affirmations = []
file_name = r'\inspire.csv'

# Collect values and append into a list
with open(source_dir+file_name) as read_obj:
    DictReader = csv.DictReader(read_obj)
    for row in DictReader:
        gratitudes.append(row["Gratitude"])
        affirmations.append(row["Affirmation"])

# Return a randomly select gratitude and affirmation
gratitude = choice(gratitudes)
affirmation = choice(affirmations)
print(f'Grateful for: {gratitude}')
print(f'Affirmation of the day: {affirmation}')        
        