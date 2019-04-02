import matplotlib.pyplot as plt
import data_handling as dh
import create_line_graph as lg
import create_bar_graph as bg

cbsdata_NL = dh.load_data_asylum_NL("Asylum NL.csv")
cbsdata_int = dh.load_data_asylum_int("Asylum International.csv")


while True:  
    choice = input("""Welcome! What do you want to do?
    1\tView asylum requests (per country of origin) to the Netherlands over time.
    2\tView asylum requests (per country of destination) over time.
    3\tView migrating population demographics (to NL) per country of origin (gender, age, etc.).
    4\tExit program.
    """)
 
# Choice Asylum requests over time
    if choice == "1":
        all_countries = ['Total Requests','Syria','Iran','China','Turkey',\
                         'Afghanistan','Irak','Eritrea','Sudan','Bosnia and Herzegovina','Romania']
        all_countries.sort()
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
                        print("That country is already in the list, please try again.")
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
                while choice != 'y' and choice != 'n':
                    choice = input("Please enter 'y' (yes) or 'n' (no).")
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
        
        
        
        
# Coice EU comparison        
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
                        print("That country is already in the list, please try again.")
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
                while choice != 'y' and choice != 'n':
                    choice = input("Please enter 'y' (yes) or 'n' (no).")
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
          
          
          
  
  # choice Demographics across countries
    elif choice == "3":
        # list of countries that will later be handed into the function defining desired countries to compare
        countries = [] 
        # all countries that are possible to compare
        all_countries = ['Total Immigration','Syria','Iran','China','Turkey',\
                                 'Afghanistan','Irak','Eritrea','Sudan','Bosnia and Herzegovina','Romania']
        all_countries.sort()

        while True:
            #ask user input which countries
            print("Which countries would you like to compare? Please choose one from this list:")
            for country in all_countries:
                print(country)
            while True:
                country_choice = input()
                if country_choice in all_countries:
                    if country_choice not in countries:
                        # if country possible to choose and hasn't been chosen yet
                        countries.append(country_choice)
                        break
                    else:
                        print("That country is already in the list. Please enter another country.")
                else:
                    print("You did not enter a country from the list, please try again.")
            print("\n")
            #display chosen countries, add more? ask user input
            print("Current countries:")
            for country in countries:
                print(country)
            countries.sort()
            if countries != all_countries:
                choice = input("Would you like to add another country? (y/n) ")
                print("\n")
                while choice != 'y' and choice != 'n':
                    choice = input("Please enter 'y' (yes) or 'n' (no).")
                if choice == 'n':
                    break
            else:
                # break if all countries possible have been chosen
                break

        #repeat process with possibilities of demographics to compare across countries
        groups = []
        all_groups = ['Age', 'Gender', 'Marital status']
        while True:
            print("These are the demographics you can choose to compare:")
            for group in all_groups:
                print(group)
            while True:
                choice = input("Please indicate a (or another) demographic you want to compare across countries \n")
                if choice in all_groups:
                    if choice not in groups:
                        groups.append(choice)
                        break
                    else:
                        print("That demographic is already being compared. Please enter another one.")
                else:
                    print("You did not enter a demographic from the list, please try again.")
            print("\n")
            print("Current demographics:")
            for group in groups:
                print(group)
            groups.sort()
            if groups != all_groups:
                choice = input("Would you like to add another demographic? (y/n) ")
                print("\n")
                while choice != 'y' and choice != 'n':
                    choice = input("Please enter 'y' (yes) or 'n' (no).")
                if choice == 'n':
                    break
            else:
                break


        # plot graph for each demographics to compare
        if 'Gender' in groups:
            #get according dataset
            gender_df = dh.load_data_gender('data_gender.csv')
            #plt graph along the list of countries chosen
            bg.create_bargraph_gender(gender_df, countries)
            plt.show()

        if 'Age' in groups:
            age_df = dh.load_data_age('data_age.csv')
            bg.create_bargraph_age(age_df, countries)
            plt.show()

        if 'Marital status' in groups:
            mar_stat_df = dh.load_data_mar_status('data_mar_status.csv')
            bg.create_bargraph_mar_status(mar_stat_df, countries)
            plt.show()

       
        
        
        
 
# choice end program
    elif choice == "4":
        print("Thank you for using this program.")
        break
    else:
        print("Choice not recognized. Try again.")    
