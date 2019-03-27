import pandas as pd
import matplotlib.pyplot as plt
import data_handling as dh
import create_line_graph as lg

cbsdata = dh.load_data_asylum("Asylum NL.csv")

while True:  
    choice = input("""Welcome! What do you want to do?
    1\tView asylum requests (per country of origin) to the Netherlands over time.
    2\tView migration numbers (per EU country of destination) over time.
    3\tView migrating population demographics (to NL) per country of origin (gender, age, etc.).
    4\tView migration flows to the Netherlands in a map for specific year.
    5\tExit program.
    """)
    
    if choice == "1":
        countries = [] 
        while True:
            print("Which countries would you like to view? Please choose one from this list:")
            print("'Total Requests','Syria','Iran','China'")
            countries.append(input())
            print("Current countries:")
            print(countries)
            choice = input("Would you like to add another country? (y/n) ")
            if choice == 'n':
                break
        
        print("What time period would you like to view? Please enter a start and end year.")
        start_year = input("Start year: ")
        end_year = input("End year: ")
        
        graph = lg.create_line_graph(cbsdata,start_year,end_year,countries)
        plt.show()
        
    elif choice == "2":
        print("To do: Create line chart.")
    elif choice == "3":
        print("To do: Create clustered bar chart.")
    elif choice == "4":
        print("To do: Create map.")
    elif choice == "5":
        print("Thank you for using this program.")
        break
    else:
        print("Choice not recognized. Try again.")  
