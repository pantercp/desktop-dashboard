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
FUNCTION THAT TAKES INPUT FROM USER AND ADDS TO OBJECTIVES DATABASE
'''

def add_objectives():

    # Adds New Objectives to the CSV Document
    lines, count = pd.read_csv(source_dir+file_name), 1
    entry = str(input('Do you have an objective to add? (Y/N)\n>>> '))
    count = 1
    while entry.upper() == 'Y':
        
        inp_category = str(input('What category is the objective?\n>>> '))
        inp_obj = str(input('What is the objective?\n>>> '))
        inp_deadline = str(input('When do you need to complete it?\n>>> '))
        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
        row_dict = {'ID':len(lines)+count,'Date': dateformat,'Category': inp_category,'Objective':inp_obj,'Deadline':inp_deadline,'Complete':'False'}
        append_dict_as_row(source_dir+file_name, row_dict, field_names)
        entry = 'N'
        count += 1
        entry = str(input('Do you have another objective to add (Y/N)?\n>>> '))
        
'''
FUNCTION FOR UPDATING COMPLETED OBJECTIVES
'''

def completed_objectives():

    user_input = input('Have you completed any objectives? (Y/N)\n>>> ')
    print()
    if user_input.upper() == 'Y':
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
    
                    with open(source_dir+file_name, 'w') as write_obj:
                        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
                        dict_writer = DictWriter(write_obj, fieldnames=field_names)
                        dw = csv.DictWriter(write_obj, delimiter=',', fieldnames=field_names)
                        dw.writeheader()              
                        dict_writer.writerows(lines)
                    print('\nCongratulations! This objective has become a milestone!')

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
completed_objectives() # Needs to change 'Complete': 'False' to valid date
# objectives = []
# collect_objectives()
# milestones = []
# collect_milestones()



# CREATE LIST OF DICTIONARIES FOR DISPLAY
# DISPLAY LIST OF CATEGORIES AND OFFER 'OTHER'
# CHOOSE HOW MANY DAYS TO FULFILL THE OBJECTIVE

'''
REQUIRED FUNCTIONS
'''
# UPDATE COMPLETED OBJECTIVES
# DISPLAY OUTSTANDING OBJECTIVES

















