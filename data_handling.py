#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:16:45 2019

@author: haenschen
"""
import pandas as pd

# importing data for asylum requests over time
def load_data_asylum(file):
    data = pd.read_csv(file, sep=";")

    # Edits years to 4 digits and creates list of years
    for i in range(3828):
        data.at[i, 'Perioden'] = data.iloc[i,2][0:4]
    
    # Takes the relevant columns
    result = data.loc[:,"Nationaliteit":"TotaalAsielverzoekenEnNareizigers_1"]
    return result


# importing data for comparisons between EU countries


# importing data for different social groups from file "name"
def load_data_groups(name):
    with open(name, "r") as file:
        df = pd.read_csv(file)
    
    # create empty dataframe with columns corresponding to the categories
    group_df = pd.Dataframe(columns=["Country of Origin", "Male", "Female", "Unmarried", "Married", "Widowed", \
                                     "Divorced", "0-10 years", "10-20 years", "20-30 years", "30-40 years",\
                                     "40-50 years", "50-60 years", "60-70 years", "70-80 years", "80-90 years" \
                                     "Female", "Male"])
    # from original data, get total per country and cut out top ten
    print("To Do: Create New Dataframe with numbers for each category per country (Top Ten Countries \
                of immigration to the Netherlands).")
    # get information from df and assign to group_df    
    
    return group_df
    

    
    


# (importing data for map)