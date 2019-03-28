import pandas as pd

def load_data_asylum_NL(file):
    data = pd.read_csv(file, sep=";")

    # Edits years to 4 digits
    for i in range(len(data)):
        data.at[i, 'Perioden'] = data.iloc[i,2][0:4]
        
    # Trims whitespace    
    data_obj = data.select_dtypes(['object'])
    data[data_obj.columns] = data_obj.apply(lambda x: x.str.strip())
    
    # Takes the relevant columns
    result = data.loc[:,"Nationaliteit":"TotaalAsielverzoekenEnNareizigers_1"]
    return result

def load_data_asylum_int(file):
    data = pd.read_csv(file, sep=";")

    # Edits years to 4 digits and creates list of years
    for i in range(len(data)):
        data.at[i, 'Perioden'] = data.iloc[i,2][0:4]
    
    # Trims whitespace    
    data_obj = data.select_dtypes(['object'])
    data[data_obj.columns] = data_obj.apply(lambda x: x.str.strip())

    # Takes the relevant columns
    result = data.loc[:,"Landen":"TotaalAsielverzoeken_1"]
    return result

# function to call data for different gender                   
def load_data_gender(dataset):
 
    # make sure data is called correctly
    try:
        with open(dataset, "r") as file:
            entire_df = pd.read_csv(file, sep=";")
            
    except Exception as err:
        print("Sorry, something went wrong. Please choose a different file or try again.")
        
    # from dataframe, select only columns that indicate gender, year, origin and number of immigrants
    df_gender = entire_df.loc[0:460, ["Geslacht", "Perioden", "Geboorteland", "Immigratie_1"]]
    
    # Edits years to 4 digits
    for i in range(460):
        df_gender.at[i, 'Perioden'] = df_gender.loc[i, 'Perioden'][0:4]
        
    # Trims whitespace    
    data_obj = df_gender.select_dtypes(['object'])
    df_gender[data_obj.columns] = data_obj.apply(lambda x: x.str.strip())
    
    
    return df_gender


# function loading the data on different age groups    
def load_data_age(dataset):
 
    # make sure data is called correctly
    try:
        with open(dataset, "r") as file:
            entire_df = pd.read_csv(file, sep=";")
            
    except Exception as err:
        print("Sorry, something went wrong. Please choose a different file or try again.")
        
        
    # from dataframe, select only columns that indicate agegroup, year, origin and number of immigrants
    df_age = entire_df.loc[0:2070, ["LeeftijdOp31December", "Perioden", "Geboorteland", "Immigratie_1"]]

    
    # Edits years to 4 digits
    for i in range(2070):
        df_age.at[i, 'Perioden'] = df_age.loc[i, 'Perioden'][0:4]
        
    # Trims whitespace    
    data_obj = df_age.select_dtypes(['object'])
    df_age[data_obj.columns] = data_obj.apply(lambda x: x.str.strip())
    
    
    return df_age

# function loading the data on different marital status
def load_data_mar_status(dataset):
 
    # make sure data is called correctly
    try:
        with open(dataset, "r") as file:
            entire_df = pd.read_csv(file, sep=";")
            
    except Exception as err:
        print("Sorry, something went wrong. Please choose a different file or try again.")
        
        
    # from dataframe, select only columns that indicate marital status, year, origin and number of immigrants
    df_mar = entire_df.loc[0:920, ["BurgerlijkeStaat", "Perioden", "Geboorteland", "Immigratie_1"]]

    
    # Edits years to 4 digits
    for i in range(920):
        df_mar.at[i, 'Perioden'] = df_mar.loc[i, 'Perioden'][0:4]
        
    # Trims whitespace    
    data_obj = df_mar.select_dtypes(['object'])
    df_mar[data_obj.columns] = data_obj.apply(lambda x: x.str.strip())
    
    
    return df_mar
