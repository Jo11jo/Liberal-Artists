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
    with open("data_groups.csv", "r") as file:
        df = pd.read_csv(file, sep=";")

    # create empty dataframe with columns corresponding to the categories
    columns=["Country of Origin", "Male", "Female", "Unmarried", "Married", "Widowed", \
                                     "Divorced", "0-10 years", "10-20 years", "20-30 years", "30-40 years",\
                                     "40-50 years", "50-60 years", "60-70 years", "70-80 years", "80-90 years" \
                                     "Female", "Male"]
    group_df = pd.DataFrame(columns=columns)
    
    # define countries to look at by code used in file
    Syria = "G008753"
    Iran = "G008634"
    China = "G008575"    
    
    # create dict with each column as key and a list as item
    # lists will include information for each country after each other (connected by index in list)
    # number of zeros varying acoording to how many countries should be looked at
    group_dict={}
    for key in columns:
        group_dict[key] = [0] * 3 # depends on how many countries should be compared
    group_dict["Country of Origin"] = ["Syria", "Iran", "China"] # add any country to this list to compare
    
    
    # loop through entries in df_file and add information from each row to lists at corresponding index
    # for each country, set an index as to where in each list the info should be added to
    for index, info in df.iterrows():
        if info["Geboorteland"] == Syria:
            country = 0
        elif info["Geboorteland"] == Iran:
            country = 1
        elif info["Geboorteland"] == China:
            country = 2
        # add more lines if more countries want to be compared
        # other unused entries
        else:
            country = 3
        
        # sort out entries for other countries
        if country < 3:
        
            # check what gender, add to gender specific list 
            if info["Geslacht"] == "3000   ":
                group_dict["Male"][country] += int(info["Immigratie_1"])
            elif info["Geslacht"] == "4000   ":
                group_dict["Female"][country] += int(info["Immigratie_1"])
            
            # if row combines both genders, check for rest of info
            elif info["Geslacht"] == "T001038":
                if info["BurgerlijkeStaat"] == "1010   ":
                    group_dict["Unmarried"][country] += int(info["Immigratie_1"])
                elif info["BurgerlijkeStaat"] == "1020   ":
                    group_dict["Married"][country] += int(info["Immigratie_1"])
                elif info["BurgerlijkeStaat"] == "1050   ":
                    group_dict["Widowed"][country] += int(info["Immigratie_1"])  
                elif info["BurgerlijkeStaat"] == "1080   ":
                    group_dict["Divorced"][country] += int(info["Immigratie_1"])  
                
                # if row combines all marital status: check for age
                elif info["BurgerlijkeStaat"] == "T001019":
                    # now check for marital status
                    if info["LeeftijdOp31December"] == "60100":
                        group_dict["0-10 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60200":
                        group_dict["10-20 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60300":
                        group_dict["20-30 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60400":
                        group_dict["30-40 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60500":
                        group_dict["40-50 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60600":
                        group_dict["50-60 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60700":
                        group_dict["60-70 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60800":
                        group_dict["70-80 years"][country] += int(info["Immigratie_1"])
                    elif info["LeeftijdOp31December"] == "60900":
                        group_dict["80-90 years"][country] += int(info["Immigratie_1"])
                
                
            
    group_df = pd.DataFrame.from_dict(group_dict)            


      
    return group_df


