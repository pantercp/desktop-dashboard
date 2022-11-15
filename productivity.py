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
REWRITE OBJECTIVES WITH A GIVEN LIST OF DICTIONARIES
'''

def rewrite_objectives(listdict):

    with open(source_dir+file_name, 'w', newline='') as write_obj:
        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dw = csv.DictWriter(write_obj, delimiter=',', fieldnames=field_names)
        dw.writeheader()              
        dict_writer.writerows(listdict)
        
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
    entry = str(input('\nDo you have an objective to add? (Y/N)\n>>> '))
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
    while user_input.upper() == 'Y':
        display_objectives() 
        obj_id = str(input('\nWhich objective did you complete? (ID num)("cancel" to quit)\n>>> '))
    
        with open(source_dir+file_name, 'r', newline='') as read_obj:
            DictReader = csv.DictReader(read_obj)
            for row in DictReader: # Don't think the order of this logic is correct
                if row['ID'] == obj_id:
                    print()
                    print(row)
                    confirm = input('\nDid you complete this one?(Y/N)\n>>> ')
                    if confirm.upper() == 'Y':
                        # Collect list of dicts from CSV document
                        with open(source_dir+file_name) as read_obj:
                            DictReader = csv.DictReader(read_obj)
                            listdict = list(DictReader)
                            # Enter information for updating document
                            completed = str(input('\nWhat date was it completed? (%D/%M/%Y)\n>>> '))
                            listdict[int(obj_id)-1]['Complete'] = completed
                        # Rewrites objectives with updated information
                        rewrite_objectives(listdict)            
                        print('\nCongratulations! This objective has become a milestone!')
                        user_input = input('\nHave you completed any other objectives? (Y/N)\n>>> ')
                elif obj_id.lower() == 'cancel':
                    user_input = 'N'
                # else:
                #     user_input = input('Do you want to select another objective? (Y/N)\n>>> ')

'''
COLLECTS MILESTONES AS A LIST OF DICTIONARIES
'''

def collect_milestones():

    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] != 'False' and row not in milestones:
                milestones.append(row)

'''
COLLECTS MILESTONES AS A LIST OF DICTIONARIES
'''

def collect_objectives():

    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] == 'False' and row not in objectives:
                objectives.append(row)
                
'''
DISPLAY OBJECTIVES WITH ID & CATEGORY
'''

def display_objectives():
    
    collect_objectives()
    print('\nYour current outstanding objectives are:\n')
    for row in objectives:
        print(row['ID'],row['Category'],'-',row['Objective'])
    
'''
DISPLAY MILESTONES WITH ID & CATEGORY
'''

def display_milestones():
    
    collect_milestones()
    print('\nYou have achieved the following milestones:\n')
    for row in milestones:
        print(row['ID'],row['Category'],'-',row['Objective'])

'''
DISPLAY BOTH OBJECTIVES & MILESTONES
'''

def display_all():
    
    display_objectives()
    display_milestones()

'''
FUNCTION TO DELETE ANY EXISTING OBJECTIVES OR MILESTONES AND REWRITE THE IDs
'''

def delete_item():
    
    repeat = input('Would you like to delete an objective or milestone? (Y/N)\n>>> ')        
    while repeat.upper() == 'Y':

        with open(source_dir+file_name) as read_obj:
            DictReader = csv.DictReader(read_obj)       
            print()
            for row in DictReader:
                print(row['ID'],row['Objective'])
         
        with open(source_dir+file_name) as read_obj:
            DictReader = csv.DictReader(read_obj)
            listdict = list(DictReader)
            
        user_input = input('\nWhich item would you like to delete? (ID num)\n>>> ')
        
        while not user_input.isnumeric():
            user_input = input('\nNot a number, please enter a valid ID number to delete\n>>> ')
            
        while int(user_input) > len(listdict) or 0 > int(user_input):
            user_input = input('\nID number does not exist, please choose an item to delete\n>>> ')
            
        confirm_input = input(f'\nAre you sure you want to delete: \n\n{listdict[int(user_input)-1]}\n\n(Y/N) >>> ')
        if confirm_input.upper() == 'Y':
            del listdict[int(user_input)-1]
            # Ammend the ID numbers so they are still sequential
            i = 1
            for row in listdict:
                row['ID'] = i
                i += 1
            # Overwrite the existing csv document 
            rewrite_objectives(listdict)
            print('\nItem has been deleted from document')
            repeat = input('\nWould you like to delete another objective or milestone? (Y/N)\n>>> ')
        else:
            repeat = input('\nWould you like to delete an objective or milestone? (Y/N)\n>>> ')


'''
THIS IS WHERE THE PROGRAM BEGINS
'''

source_dir = os.getcwd()
file_name = r'\objectives.csv'

today = date.today()
dateformat = today.strftime("%d/%m/%Y")

print('\nAccess extra function features using:\n\ndisplay_objectives()\
      \ndisplay_milestones()\ndisplay_all()\ndelete_item()')

objectives = []
milestones = []
# display_all()
# add_objectives()
# completed_objectives()
# display_objectives()
# display_milestones()
# delete_item()

# CREATE FUNCTION TO CHANGE AN ITEM IN CSV DOC

def change_item():

    with open(source_dir+file_name) as read_obj:
        DictReader = csv.DictReader(read_obj)
        listdict = list(DictReader)
        print()
        
    for row in listdict:
        print(row['ID'],row['Category'],row['Objective'],row['Deadline'])
        
    # Conditionals still required
    choice = input('\nWhich item would you like to change? (ID num)\n>>> ')
    print()
    print(listdict[int(choice)-1])
    print()
    for key in listdict[0]:
        print(key)
            
        
    column = input('\nWhich detail would you like to change? ("Q" to quit)\n>>> ')
    
    if column in listdict[0].keys():
        print('\nWould you like to change:\n>>> ',end='')
        print(listdict[int(choice)-1][column])
        confirm = input('\n(Y/N) >>> ')
        if confirm.upper() == 'Y':
            update = input('\nPlease enter new information\n>>> ')
            listdict[int(choice)-1][column] = update
            confirm = input('\nWould you like to irreversibly update your list? (Y/N)\n>>> ')
            if confirm.upper() == 'Y':
                rewrite_objectives(listdict)
    else:
        change = input('\nNot a valid choice, would you like to try again? (Y/N)\n>>> ')
        if change.upper() == 'Y':
            change_item()
        else:
            print('\nExiting and returning to program...')
        


# change_item()

# CREATE LIST OF DICTIONARIES FOR DISPLAY
# CHOOSE HOW MANY DAYS TO FULFILL THE OBJECTIVE

'''
REQUIRED FUNCTIONS
'''
# CREATE A FUNCTION THAT DELETES A ROW AND AMMENDS ID NUMBERS
# DISPLAY OUTSTANDING OBJECTIVES

















