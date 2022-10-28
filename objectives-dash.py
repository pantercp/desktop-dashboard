# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:03:50 2022

@author: Ronaldo
"""

import os
import csv
from csv import DictWriter
import pandas as pd


def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

source_dir = os.getcwd()
file_name = r'\objectives.csv'

# Adds New Objectives to the CSV Document
entry = str(input('Do you have an objective to add (Y/N)?\n>>> '))
while entry.upper() == 'Y':
    
    lines = pd.read_csv(source_dir+file_name)
    inp_lines = len(lines)+1
    inp_date = str(input('What is the date?\n>>> '))
    inp_category = str(input('What category is the objective?\n>>> '))
    inp_obj = str(input('What is the objective?\n>>> '))
    inp_deadline = str(input('When do you need to complete it?\n>>> '))
    field_names = ['ID','Date','Category','Objective','Deadline','Complete']
    row_dict = {'ID':inp_lines,'Date': inp_date,'Category': inp_category,'Objective':inp_obj,'Deadline':inp_deadline,'Complete':'False'}
    append_dict_as_row(source_dir+file_name, row_dict, field_names)
    entry = 'N'
    entry = str(input('Do you have another objective to add (Y/N)?\n>>> '))


with open(source_dir+file_name, 'r', newline='') as read_obj:
    DictReader = csv.DictReader(read_obj)
    for row in DictReader:
        if row['Complete'] != 'False':
            print(row)









# i = 1
# Dict = {}
# ID = [1,2,3,4,5,6,7,8]


#         print(row)
#         Dict = {ID[]}

        # date_col = {'Date': []}
        # categ_col = {'Category': []}
        # obj_col = {'Objective': []}
        # for record in DictReader:
        #     date_col['Date'].append(record['Date'])
        #     categ_col['Category'].append(record['Category'])
        #     obj_col['Objective'].append(record['Objective'])

# merged = {**date_col, **categ_col, **obj_col}



# with open(source_dir+file_name, 'r', newline='') as read_obj:
#     reader = csv.reader(read_obj)
#     for row in reader:
#         if reader.line_num == 1:
#             continue
#         else:
#             print('Row #' + str(reader.line_num) + ' ' + str(row))



