

while True:
    
    choice = input("""What do you want to do?
    1\tView migration numbers (per country of origin) to the Netherlands over time.
    2\tView migration numbers (per EU country of destination) over time.
    3\tView migrating population demographics (to NL) per country of origin (gender, age, etc.).
    4\tView migration flows to the Netherlands in a map for specific year.
    5\tExit program.
    """)
    
    if choice == "1":
        print("To do: Load corresponding CBS data set.")
        print("To do: Create line chart.")
    elif choice == "2":
        print("To do: Load corresponding CBS data set.")
        print("To do: Create line chart.")
    elif choice == "3":
        print("To do: Load corresponding CBS data set.")
        
        population = input("""Which social groups do you want to compare?
        1\tCompare age groups
        2\tCompare marital status
        3\tCompare gender
        4\tExit program""")
        
        if population == "1":
            print("To do: Create bar chart clustered by age group.")
        elif population == "2":
            print("To do: Create bar chart clustered by marital status.")
        elif population == "3":
            print("To do: Create bar chart clustered by gender.")
        elif population == "4":
            print("Thank you for using this program.")
            break
        else:
            print("Choice not recognized. Try again.")
        
        
    elif choice == "4":
        print("To do: Load corresponding CBS data set.")
        print("To do: Create map.")
    elif choice == "5":
        print("Thank you for using this program.")
        break
    else:
        print("Choice not recognized. Try again.")    
