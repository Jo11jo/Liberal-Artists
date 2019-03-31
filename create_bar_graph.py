

import matplotlib.pyplot as plt


def create_bargraph_gender(dataframe, country_list):
    # Dictionary that relates country to country code
    country_dict = {'Total Numbers':'T001175','Syria':'G008753','Iran':'G008634',\
                    'China':'G008575','Turkey':'G008766','Afghanistan':'G008533','Irak':'G008633',\
                    'Eritrea':'G008597','Sudan':'G008746','Bosnia and Herzegovina':'G008559',\
                    'Romania':'G008723'}
    
    n = len(country_list)
    
    # list that later contains all important info to be plotted
    graph_list = []
    
        
    
    # get gender distribution per country
    for country in country_list:
        # choose data only for specific country
        df_chosen = dataframe[dataframe['Geboorteland'] == country_dict[country]]
        Male = 0
        Female = 0
    
        
        # sum immigration numbers from all years, assign to gender variables
        for index, year in df_chosen.iterrows():
            if year['Geboorteland'] == country_dict[country]:
                if year['Geslacht'] == 3000:
                    Male += year['Immigratie_1']
                elif year['Geslacht'] == 4000:
                    Female += year['Immigratie_1']
        
        # nest lists into graph_list that can be graphed later
        # one nested item includes country's name, gender and number of immigrants
        male_list = [country, 'Male', Male]
        graph_list.append(male_list)
        female_list = [country, 'Female', Female]
        graph_list.append(female_list)
    
    
    
    # set up info for graph
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # space between clusters
    space = 0.3
    
    gender = ['Male', 'Female']
    x = len(gender)
    width = (1 - space) / x
    
    
    # graph each gender
    for i, gend in enumerate(gender):
        numb = [] # y axis
        pos = [] # x axis
        
        #get list with numbers for each gender individually 
        for z in range(n*2):
            #choose numbers in list for right gender
            if graph_list[z][1] == gend:
                numb.append(graph_list[z][2])
                
        # get integers for each bar - x axis
        j_list =[] #later use for x-axis lalbelling
        for j in range(1,len(country_list)+1):
            j_list.append(j-(width/2)) # xtickts will be in the middle of a cluster
            pos.append(j - (1 - space) / 2. + i * width)
        ax.bar(pos, numb, width=width)
    
    # adjust entire graph
    ax.set_xticks(j_list)
    ax.set_xticklabels(country_list)
    plt.setp(plt.xticks()[1], rotation=90)
    ax.set_ylabel("Number of Immigrants")
    ax.set_xlabel("Country")
    plt.title('Gender Distribution for Immigrants coming to the Netherlands per country')
    ax.legend(gender)

            
        
        
        
        
        
        
def create_bargraph_age(dataframe, country_list):
    # Dictionary that relates country to country code
    country_dict = {'Total Numbers':'T001175','Syria':'G008753','Iran':'G008634',\
                        'China':'G008575','Turkey':'G008766','Afghanistan':'G008533','Irak':'G008633',\
                        'Eritrea':'G008597','Sudan':'G008746','Bosnia and Herzegovina':'G008559',\
                        'Romania':'G008723'}
    
    i = 0    
    n = len(country_list)
    fig = plt.figure()
    # plot each country individually
    for country in country_list:
        i +=1
        # choose data only for specific country
        df_chosen = dataframe[dataframe['Geboorteland'] == country_dict[country]]
        younger10 = 0
        younger20 = 0
        younger30 = 0
        younger40 = 0
        younger50 = 0
        younger60 = 0
        younger70 = 0
        younger80 = 0
        younger90 = 0
        
        # sum immigration numbers from all years
        for index, year in df_chosen.iterrows():
            if year['Geboorteland'] == country_dict[country]:
                if year['LeeftijdOp31December'] == 60100:
                    younger10 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60200:
                    younger20 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60300:
                    younger30 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60400:
                    younger40 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60500:
                    younger50 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60600:
                    younger60 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60700:
                    younger70 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60800:
                    younger80 += year['Immigratie_1']
                elif year['LeeftijdOp31December'] == 60900:
                    younger90 += year['Immigratie_1']
         
    
        # set layout for graph    
        x = list(range(9))
        data = [younger10, younger20, younger30, younger40, younger50, younger60, younger70, \
                younger80, younger90]       
        labels = ['0 - 10', '10 - 20', '20 - 30', '30 - 40', '40 - 50',\
                  '50 - 60', '60 - 70', '70 - 80', '80 - 90']
        
        fig.add_subplot(n, 1, i)
        plt.bar(x, data, label=country)
        plt.ylabel(f'Immigrants \n to {country}')
    
    # plot all next to each other
    plt.subplots_adjust(bottom=0, top=2, hspace=0)
    plt.xticks(x, labels, rotation='vertical')
    plt.xlabel('Age Distribution in years for Immigrants coming to the Netherlands per country')
    plt.show()
    

            
        
        
        
        
        
        
def create_bargraph_mar_status(dataframe, country_list):
    # Dictionary that relates country to country code
    country_dict = {'Total Numbers':'T001175','Syria':'G008753','Iran':'G008634',\
                        'China':'G008575','Turkey':'G008766','Afghanistan':'G008533','Irak':'G008633',\
                        'Eritrea':'G008597','Sudan':'G008746','Bosnia and Herzegovina':'G008559',\
                        'Romania':'G008723'}
        
    
    n = len(country_list)
    
    # storage for data on all countries
    data_unmarried = []
    data_married = []
    data_widowed = []
    data_divorced = []
    
    # get data for each country individually
    for country in country_list:
        # choose data only for specific country
        df_chosen = dataframe[dataframe['Geboorteland'] == country_dict[country]]
        unmarried = 0
        married = 0
        widowed = 0
        divorced = 0
        
        # sum immigration numbers from all years
        for index, year in df_chosen.iterrows():
            if year['Geboorteland'] == country_dict[country]:
                if year['BurgerlijkeStaat'] == 1010:
                    unmarried += year['Immigratie_1']
                elif year['BurgerlijkeStaat'] == 1020:
                    married += year['Immigratie_1']
                elif year['BurgerlijkeStaat'] == 1050:
                    widowed += year['Immigratie_1']
                elif year['BurgerlijkeStaat'] == 1080:
                    divorced += year['Immigratie_1']
      
        # add data for country to list
        data_unmarried.append(unmarried) 
        data_married.append(married)
        data_widowed.append(widowed)
        data_divorced.append(divorced)
    
    
    # set up graph delimiters
    x = list(range(n))
    labels = ["Unmarried", "Married", "Widowed", "Divorced"]
    
    # graph each marital status as stacken on top of another
    p1 = plt.bar(x, data_unmarried)
    p2 = plt.bar(x, data_married, bottom=data_unmarried)
    bottom = [sum(x) for x in zip(data_unmarried, data_married)]
    p3 = plt.bar(x, data_widowed, bottom=bottom)
    bottom = [sum(x) for x in zip(data_unmarried, data_married, data_widowed)]
    p4 = plt.bar(x, data_divorced, bottom=bottom)
    
    # adjust graph display
    plt.xticks(x, country_list, rotation='vertical')
    plt.legend(labels)
    plt.title('Distribution of marital status for Immigrants coming to the Netherlands per country')
    plt.show()
