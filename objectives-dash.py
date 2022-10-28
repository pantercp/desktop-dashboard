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
    lines = pd.read_csv(source_dir+file_name)
    entry = str(input('Do you have an objective to add? (Y/N)\n>>> '))
    while entry.upper() == 'Y':
    
        inp_category = str(input('What category is the objective?\n>>> '))
        inp_obj = str(input('What is the objective?\n>>> '))
        inp_deadline = str(input('When do you need to complete it?\n>>> '))
        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
        row_dict = {'ID':len(lines)+1,'Date': dateformat,'Category': inp_category,'Objective':inp_obj,'Deadline':inp_deadline,'Complete':'False'}
        append_dict_as_row(source_dir+file_name, row_dict, field_names)
        entry = 'N'
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
                    confirm = input('\nDid you complete this one?(Y/N)\n')
                    if confirm.upper() == 'Y':
                        fulfilled = input('\nDate completed? (%d/%m/%Y)\n>>> ')
                        row['Complete'] = fulfilled
  

'''
COLLECTS MILESTONES AS A LIST OF DICTIONARIES
'''

def collect_milestones():

    milestones = []

    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            if row['Complete'] != 'False':
                milestones.append(row)


'''
THIS IS WHERE THE PROGRAM BEGINS
'''

source_dir = os.getcwd()
file_name = r'\objectives.csv'

today = date.today()
dateformat = today.strftime("%d/%m/%Y")


add_objectives()
completed_objectives()
collect_milestones()



# CREATE LIST OF DICTIONARIES FOR DISPLAY
# DISPLAY LIST OF CATEGORIES AND OFFER 'OTHER'
# CHOOSE HOW MANY DAYS TO FULFILL THE OBJECTIVE

'''
REQUIRED FUNCTIONS
'''
# UPDATE COMPLETED OBJECTIVES
# DISPLAY OUTSTANDING OBJECTIVES

















