import pandas as pd
import matplotlib.pyplot as plt
import data_handling as dh
import create_line_graph as lg

cbsdata_NL = dh.load_data_asylum_NL("Asylum NL.csv")
cbsdata_int = dh.load_data_asylum_int("Asylum International.csv")

all_countries = ['Total Requests','Syria','Iran','China','Turkey',\
                         'Afghanistan','Irak','Eritrea','Sudan','Bosnia and Herzegovina','Romania']
all_countries.sort()

while True:  
    choice = input("""Welcome! What do you want to do?
    1\tView asylum requests (per country of origin) to the Netherlands over time.
    2\tView asylum requests (per country of destination) over time.
    3\tView migrating population demographics (to NL) per country of origin (gender, age, etc.).
    4\tView migration flows to the Netherlands in a map for specific year.
    5\tExit program.
    """)
    
    if choice == "1":
        
        countries = [] 

        while True:
            print("Which countries would you like to view? Please choose one from this list:")
            for country in all_countries:
                print(country)
            while True:
                country_choice = input()
                if country_choice in all_countries:
                    if country_choice not in countries:
                        countries.append(country_choice)
                        break
                    else:
                        print("That country is already in the list.")
                else:
                    print("You did not enter a country from the list, please try again.")
            print("\n")
            print("Current countries:")
            for country in countries:
                print(country)
            countries.sort()
            if countries != all_countries:
                choice = input("Would you like to add another country? (y/n) ")
                print("\n")
                if choice == 'n':
                    break
            else:
                break
        
        while True:
            print("What time period would you like to view? Please enter a start and end year (between 1975 and 2018).")
            while True:
                try:
                    start_year = int(input("Start year: "))
                    break
                except:
                    print("You did not enter an integer!")
            if start_year < 1975 or start_year > 2017:
                print("You entered an invalid start year, please try again.")
                print("\n")
                continue
            while True:
                try:
                    end_year = int(input("End year: "))
                    break
                except:
                    print("You did not enter an integer!")     
            if end_year < 1975 or end_year > 2018:
                print("You entered an invalid end year, please try again.")
                print("\n")
                continue
            if end_year <= start_year:
                print("The end year must be after the start year!")
                print("\n")
                continue
            break            
        
        graph = lg.line_graph_NL(cbsdata_NL,start_year,end_year,countries)
        plt.show()
        
    elif choice == "2":
        
        countries = [] 
        all_countries = ['The Netherlands','EU Total','Belgium','Denmark','Germany','France',\
                         'Greece','Hungary','Italy','Czech Republic','United Kingdom','Norway',\
                         'Canada','United States of America']
        all_countries.sort()
        while True:
            print("Which countries would you like to view? Please choose one from this list:")
            for country in all_countries:
                print(country)
            while True:
                country_choice = input()
                if country_choice in all_countries:
                    if country_choice not in countries:
                        countries.append(country_choice)
                        break
                    else:
                        print("That country is already in the list.")
                else:
                    print("You did not enter a country from the list, please try again.")
            print("\n")
            print("Current countries:")
            for country in countries:
                print(country)
            countries.sort()
            if countries != all_countries:
                choice = input("Would you like to add another country? (y/n) ")
                print("\n")
                if choice == 'n':
                    break
            else:
                break
        
        while True:
            print("What time period would you like to view? Please enter a start and end year (between 2008 and 2016).")
            while True:
                try:
                    start_year = int(input("Start year: "))
                    break
                except:
                    print("You did not enter an integer!")
            if start_year < 2008 or start_year > 2015:
                print("You entered an invalid start year, please try again.")
                print("\n")
                continue
            while True:
                try:
                    end_year = int(input("End year: "))
                    break
                except:
                    print("You did not enter an integer!")     
            if end_year < 2008 or end_year > 2016:
                print("You entered an invalid end year, please try again.")
                print("\n")
                continue
            if end_year <= start_year:
                print("The end year must be after the start year!")
                print("\n")
                continue
            break            
        
        graph = lg.line_graph_int(cbsdata_int,start_year,end_year,countries)
        plt.show()     
                                
    elif choice == "3":
        print("To do: Create clustered bar chart.")
    elif choice == "4":
        print("To do: Create map.")
    elif choice == "5":
        print("Thank you for using this program.")
        break
    else:
        print("Choice not recognized. Try again.")    
