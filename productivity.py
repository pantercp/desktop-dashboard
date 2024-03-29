# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:03:50 2022

@author: Ronaldo
"""

import os
import csv
from csv import DictWriter
from datetime import date


'''
ADDS NEW DICTIONARY AS A ROW TO CSV
'''

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as row in the csv
        dict_writer.writerow(dict_of_elem)

'''
REWRITE OBJECTIVES WITH A GIVEN LIST OF DICTIONARIES
'''

def rewrite_objectives(listdict):

    # Open file in write mode
    with open(source_dir+file_name, 'w', newline='') as write_obj:
        # Add keys for dict to top row of CSV
        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dw = csv.DictWriter(write_obj, delimiter=',', fieldnames=field_names)
        dw.writeheader()              
        dict_writer.writerows(listdict) # Add key's values to csv
        
'''
DISPLAYS CATEGORY OPTIONS AND RETURNS CHOICE
'''

def category_choice():
    
    category = []

    with open(source_dir+file_name) as read_obj:
        DictReader = csv.DictReader(read_obj) # Read csv as a dictionary
        for row in DictReader:
            # Adds existing categories without duplicates
            if row['Category'] not in category:
                category.append(row['Category'])
    
    i = 0
    print()
    # Displays options with index number
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

    # Loop instigated for choosing to add an objective
    entry = str(input('\nDo you have an objective to add? (Y/N)\n>>> '))
    while entry.upper() == 'Y':
        
        inp_category = category_choice() # Returns category choice
        inp_obj = str(input('\nWhat is the objective?\n>>> '))
        inp_deadline = str(input('\nWhen do you need to complete it?\n>>> '))
        # Keys for Dictionary in order to add it to existing csv structure
        field_names = ['ID','Date','Category','Objective','Deadline','Complete']
        
        # Need to get maximum value of ID
        with open(source_dir+file_name) as read_obj:
            DictReader = csv.DictReader(read_obj)
            listdict = list(DictReader) # Create list of existing csv content
        max = 0
        for row in listdict:
            if int(row["ID"]) > int(max):
                max = row["ID"] # Gives the highest current ID in csv
        
        row_dict = {'ID':int(max)+1,'Date': dateformat,'Category': inp_category,'Objective':inp_obj,'Deadline':inp_deadline,'Complete':'FALSE'}
        # Adds new objectives key values into csv
        append_dict_as_row(source_dir+file_name, row_dict, field_names)
        entry = 'N'
        entry = str(input('\nDo you have another objective to add (Y/N)?\n>>> '))
        
'''
FUNCTION FOR UPDATING COMPLETED OBJECTIVES
'''

def completed_objectives():

    user_input = input('\nHave you completed any objectives? (Y/N)\n>>> ')
    while user_input.upper() == 'Y':
        display_objectives() # Lists all currently outstanding objectives
        obj_id = str(input('\nWhich objective did you complete? (ID num)("cancel" to quit)\n>>> '))
    
        with open(source_dir+file_name, 'r', newline='') as read_obj:
            DictReader = csv.DictReader(read_obj)
            for row in DictReader:
                if row['ID'] == obj_id:
                    print()
                    print(row) # Display selected objective
                    confirm = input('\nDid you complete this one?(Y/N)\n>>> ')
                    if confirm.upper() == 'Y':
                        # Collect list of dicts from CSV document
                        with open(source_dir+file_name) as read_obj:
                            DictReader = csv.DictReader(read_obj)
                            listdict = list(DictReader) # Make list of dicts for overwriting
                            # Enter information for updating document
                            completed = str(input('\nWhat date was it completed? (%D/%M/%Y)\n>>> '))
                            # Locates the dictionary in objectives list and deletes it to keep the
                            # display functions up to date
                            dict_index = next((index for (index, d) in enumerate(objectives) \
                                               if d["Objective"] == f'{row["Objective"]}'), None)
                            del objectives[dict_index]
                            
                            # Find existing objective in list dict and update value
                            for i, d in enumerate(listdict): # Go through list of dicts
                                if d.get("ID") == row["ID"]: # Find matching ID
                                    print(f"The index of the dictionary with ID {row['ID']} is {i}")
                                    listdict[i]["Complete"] = completed
                                    # Rewrites objectives with updated information
                                    rewrite_objectives(listdict)            
                                    print('\nCongratulations! This objective has become a milestone!')
                                    user_input = input('\nHave you completed any other objectives? (Y/N)\n>>> ')
                                    break
                            else:
                                print("Not found index of dictionaries ID")

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
            # Adds milestones to list and ensures there are no duplicates
            if row['Complete'] != 'FALSE' and row not in milestones:
                milestones.append(row)
'''
COLLECTS MILESTONES AS A LIST OF DICTIONARIES
'''

def collect_objectives():

    with open(source_dir+file_name, 'r', newline='') as read_obj:
        DictReader = csv.DictReader(read_obj)
        for row in DictReader:
            # Adds objectives to list and ensures there are no duplicates
            if row['Complete'] == 'FALSE' and row not in objectives:
                objectives.append(row)
                
'''
DISPLAY OBJECTIVES WITH ID & CATEGORY
'''

def display_objectives():
    
    collect_objectives()
    print('\nYour current outstanding objectives are:\n')
    for row in objectives:
        # Prints desired key values from outstanding objectives
        print(row['ID'],row['Category'],'-',row['Objective'])
    
'''
DISPLAY MILESTONES WITH ID & CATEGORY
'''

def display_milestones():
    
    collect_milestones()
    print('\nYou have achieved the following milestones:\n')
    for row in milestones:
        # Prints desired key values from current milestones
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
    
    repeat = input('\nWould you like to delete an objective or milestone? (Y/N)\n>>> ')        
    while repeat.upper() == 'Y':

        with open(source_dir+file_name) as read_obj:
            DictReader = csv.DictReader(read_obj)       
            print()
            i = 0
            for row in DictReader:
                print(i,row['Objective']) # Displays all objectives & milestones
                i += 1
         
        with open(source_dir+file_name) as read_obj:
            DictReader = csv.DictReader(read_obj)
            listdict = list(DictReader) # Preps a list of all obj & milestones
            
        user_input = input('\nWhich item would you like to delete? (Index num)\n>>> ')
        
        while not user_input.isnumeric(): # Ensure entry is numeric
            user_input = input('\nNot a number, please enter a valid ID number to delete\n>>> ')
            
        while int(user_input) > len(listdict) or 0 > int(user_input): # Ensures valid index
            user_input = input('\nID number does not exist, please choose an item to delete\n>>> ')
            
        # Confirmation of information selected for deleting
        confirm_input = input(f'\nAre you sure you want to delete: \n\n{listdict[int(user_input)]}\n\n(Y/N) >>> ')
        if confirm_input.upper() == 'Y':
            
            if listdict[int(user_input)] in objectives:
                # Locates the dictionary in objectives list
                dict_index = next((index for (index, d) in enumerate(objectives) \
                                   if d["Objective"] == f'{listdict[int(user_input)]["Objective"]}'), None)
                del objectives[dict_index] # Keeps display functions up to date

            if listdict[int(user_input)] in milestones:
                # Locates the dictionary in objectives list
                dict_index = next((index for (index, d) in enumerate(milestones) \
                                   if d["Objective"] == f'{listdict[int(user_input)]["Objective"]}'), None)
                del milestones[dict_index] # Keeps display functions up to date
            
            del listdict[int(user_input)]

            # Overwrite the existing csv document 
            rewrite_objectives(listdict)
            print('\nItem has been deleted from document')
            repeat = input('\nWould you like to delete another objective or milestone? (Y/N)\n>>> ')
        else:
            repeat = input('\nWould you like to delete an objective or milestone? (Y/N)\n>>> ')


'''
FUNCTION TO CHANGE AN ITEM IN CSV DOC
'''

def change_item():

    repeat = "Y"
    while repeat.upper() == "Y":

        with open(source_dir+file_name) as read_obj:
            DictReader = csv.DictReader(read_obj)
            listdict = list(DictReader) # Preps list for changing csv content
            print()
        
        i = 0
        for row in listdict: # Display choices for the change
            print(i,row['Category'],row['Objective'],row['Deadline'])
            i += 1
            
        choice = input('\nWhich item would you like to change? (ID num)\n>>> ')
        if choice.isnumeric() and int(choice) <= len(listdict)-1:
            print(f'\n{listdict[int(choice)]}\n') # Displays all info for choice
            for key in listdict[0]:
                print(key)         
            category = input('\nWhich detail would you like to change? ("Q" to quit)\n>>> ')
        else:
            print("\nNot a valid entry!\n") # Gives chance to retry non-valid choice
            confirm = input("Do you still wish to change an item? (Y/N)\n>>> ")
            if confirm.upper() == "Y":
                change_item()
            else:
                repeat = "N"
                break
    
        if category.capitalize() in listdict[0].keys():
            print('\nWould you like to change:\n>>> ',end='')
            # Display information of entry requested for change
            print(listdict[int(choice)][category.capitalize()])
            confirm = input('\n(Y/N) >>> ')
            if confirm.upper() == 'Y':
                update = input('\nPlease enter new information\n>>> ')
                # Add new information to the key's value
                listdict[int(choice)][category.capitalize()] = update
                confirm = input('\nWould you like to irreversibly update your list? (Y/N)\n>>> ')
                if confirm.upper() == 'Y':
                    rewrite_objectives(listdict) # Rewrites csv with updated list
                    print(f'\nYour changes have been updated:\n\n{listdict[int(choice)]}')            
                    
                else:
                    print('\nDid not press "Y"...') # No confirmation, option to retry
                    change = input('\nWould you like to try again? (Y/N)\n>>> ')
                    if change.upper() == 'Y':
                        change_item()
                    else:
                        print('\nExiting and returning to program...')
                        break
            else:
                print('\nDid not press "Y"...')
                change = input('\nWould you like to try again? (Y/N)\n>>> ')
                if change.upper() == 'Y':
                    change_item()
                else:
                    print('\nExiting and returning to program...')
                    break
        else:
            change = input('\nNot a valid choice, would you like to try again? (Y/N)\n>>> ')
            if change.upper() == 'Y':
                change_item()
            else:
                print('\nExiting and returning to program...')
                break

'''
PROGRAM RUNS FROM HERE
'''

source_dir = "C:\\Users\\Ronaldo\\OneDrive\\Python\\git\\ninetynine"
file_name = r'\objectives.csv'

today = date.today()
dateformat = today.strftime("%d/%m/%Y")

objectives = []
milestones = []

print('\nWelcome to your Productivity Dashboard!')

#
options = ["Display All","Display Objectives","Display Milestones","Add Objectives","Completed\
 Objectives", "Delete Item","Change Item"]
            
repeat = "Y"
while repeat.upper() == "Y":
    i = 0
    print("\nYour dashboard options are the following:\n")
    for option in options:
        print(i, option)
        i += 1
    choice = input(f'\nEnter an option 0 to {len(options)-1} or hit [ENTER] to continue\n>>> ')
    
    # Gives the user choice of running functions before continuing into the program
    if choice.isnumeric() and int(choice) <= len(options)-1:
        if int(choice) == 0:
            print("Option 0")
            display_all()
        elif int(choice) == 1:
            print("Option 1")
            display_objectives()
        elif int(choice) == 2:
            print("Option 2")
            display_milestones()
        elif int(choice) == 3:
            print("Option 3")
            add_objectives()
        elif int(choice) == 4:
            print("Option 4")
            completed_objectives()
        elif int(choice) == 5:
            print("Option 5")
            delete_item()
        elif int(choice) == 6:
            print("Option 6")
            change_item()
    else:
        print("\nContinuing to Inspiration Image generator...")
        repeat = "N"



'''
LIST OF FUNCTIONS FOR TESTING
'''

# display_all()
# add_objectives()
# completed_objectives()
# display_objectives()
# display_milestones()
# delete_item()
# change_item()


'''
REQUIRED FUNCTIONS
'''








