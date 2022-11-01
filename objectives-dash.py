# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:03:50 2022

@author: Ronaldo
"""

import os
import csv
from csv import DictWriter
from datetime import date
import pandas as pd


'''
ADDS NEW DICTIONARY AS A ROW TO CSV
'''

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

'''
DISPLAYS CATEGORY OPTIONS AND RETURNS CHOICE
'''

def category_choice():
# Adds existing categories without duplicates
    category = []

    with open(source_dir+file_name) as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Category'] not in category:
                category.append(row['Category'])
    
    # Displays options with index number
    i = 0
    print()
    for word in category:   
        print(i, word)
        i += 1
    
    # Repeats input request until valid category entry returned
    repeat = 'Y'
    while repeat == 'Y':
        category_input = input('\nEnter category number or type "other"\n>>> ')
        repeat = 'N'
        if category_input.isnumeric() and int(category_input)<=(len(category))-1:
            category_output = (category[int(category_input)])
        elif category_input.isnumeric() and int(category_input)>(len(category))-1:
            print('\nNumber category does not exist!')
            repeat = 'Y'
        elif category_input.lower() == 'other':
            category_output = input('\nEnter your category\n>>> ')
            repeat = 'N'
        else:
            print('\nNot a valid entry')
            repeat = 'Y'
        
    return category_output


'''
FUNCTION THAT TAKES INPUT FROM USER AND ADDS TO OBJECTIVES DATABASE
'''

def add_objectives():

    # Adds New Objectives to the CSV Document
    lines, count = pd.read_csv(source_dir+file_name), 1
    entry = str(input('Do you have an objective to add? (Y/N)\n>>> '))
    count = 1
    while entry.upper() == 'Y':
        
        inp_category = category_choice()
        inp_obj = str(input('\nWhat is the objective?\n>>> '))
        inp_deadline = str(input('\nWhen do you need to complete it?\n>>> '))
        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
        row_dict = {'ID':len(lines)+count,'Date': dateformat,'Category': inp_category,'Objective':inp_obj,'Deadline':inp_deadline,'Complete':'False'}
        append_dict_as_row(source_dir+file_name, row_dict, field_names)
        entry = 'N'
        count += 1
        entry = str(input('\nDo you have another objective to add (Y/N)?\n>>> '))
        
'''
FUNCTION FOR UPDATING COMPLETED OBJECTIVES
'''

def completed_objectives():

    user_input = input('\nHave you completed any objectives? (Y/N)\n>>> ')
    print()
    while user_input.upper() == 'Y':
        with open(source_dir+file_name, 'r', newline='') as read_obj:
            DictReader = csv.DictReader(read_obj)
            for row in DictReader:
                if row['Complete'] == 'False':
                    print(row['ID'],row['Objective'])
            print()
    
        obj_id = str(input('Which objective did you complete? (ID num)\n>>> '))
        print()
    
        with open(source_dir+file_name, 'r', newline='') as read_obj:
            DictReader = csv.DictReader(read_obj)
            for row in DictReader:
                if row['ID'] == obj_id:
                    print(row)
                    confirm = input('\nDid you complete this one?(Y/N)\n>>> ')
                    if confirm.upper() == 'Y':
                        with open(source_dir+file_name) as read_obj:
                            DictReader = csv.DictReader(read_obj)
                            lines = list(DictReader)
                            print()
                            completed = str(input('What date was it completed? (%D/%M/%Y)\n>>> '))
                            lines[int(obj_id)-1]['Complete'] = completed
        
                        with open(source_dir+file_name, 'w', newline='') as write_obj:
                            field_names = ['ID','Date','Category','Objective','Deadline','Complete']
                            dict_writer = DictWriter(write_obj, fieldnames=field_names)
                            dw = csv.DictWriter(write_obj, delimiter=',', fieldnames=field_names)
                            dw.writeheader()              
                            dict_writer.writerows(lines)
                        print('\nCongratulations! This objective has become a milestone!')
                        user_input = input('\nHave you completed any other objectives? (Y/N)\n>>> ')

'''
COLLECTS MILESTONES AS A LIST OF DICTIONARIES
'''

def collect_milestones():

    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] != 'False':
                milestones.append(row)

'''
COLLECTS MILESTONES AS A LIST OF DICTIONARIES
'''

def collect_objectives():

    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] == 'False':
                objectives.append(row)

'''
THIS IS WHERE THE PROGRAM BEGINS
'''

source_dir = os.getcwd()
file_name = r'\objectives.csv'

today = date.today()
dateformat = today.strftime("%d/%m/%Y")


add_objectives()
completed_objectives()
# objectives = []
# collect_objectives()
# milestones = []
# collect_milestones()

            


# CREATE LIST OF DICTIONARIES FOR DISPLAY
# CHOOSE HOW MANY DAYS TO FULFILL THE OBJECTIVE

'''
REQUIRED FUNCTIONS
'''
# CREATE A FUNCTION THAT DELETES A ROW AND AMMENDS ID NUMBERS
# DISPLAY OUTSTANDING OBJECTIVES

















