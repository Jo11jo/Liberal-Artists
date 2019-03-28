import matplotlib.pyplot as plt

def line_graph_NL(cbsdata,start_year,end_year,countries):
    
    # Dictionary that relates country to country code
    country_dict = {'Total Requests':'T001059','Syria':'NAT9444','Iran':'NAT9351',\
                    'China':'NAT9310','Turkey':'NAT9458','Afghanistan':'NAT9278','Irak':'NAT9350',\
                    'Eritrea':'NAT9326','Sudan':'NAT9437','Bosnia and Herzegovina':'NAT9298',\
                    'Romania':'NAT9417'}
    
    for country in countries:     
        # Creates list of years and a copy
        years = []
        trimmed_years = []
        i = int(start_year)
        while i <= int(end_year):
            years.append(i)
            trimmed_years.append(i)
            i = i + 1     
               
        # Trims the dataframe down to only the required country
        country_data = cbsdata[cbsdata['Nationaliteit']==country_dict[country]]
    
        # Creates a list of asylum requests per year for that country. If there is
        # no data available, the data point is removed. 
        asylum_requests = []
        for i in years:
            try:
                asylum_requests.append(int(country_data[country_data['Perioden']==str(i)].iloc[0,2]))
            except:
                trimmed_years.remove(i)        
    
        # Plot the asylum requests over time for the country
        plt.plot(trimmed_years,asylum_requests,label=country)
    
    plt.xlabel('Years')
    xint = []
    locs, labels = plt.xticks()
    for each in locs:
        xint.append(int(each))
    plt.xticks(xint)
    plt.xlim(start_year, end_year)
    plt.ylabel('Asylum Requests')
    plt.title('Asylum Requests to the Netherlands')
    plt.legend()
    
def line_graph_int(cbsdata,start_year,end_year,countries):
    
    # Dictionary that relates country to country code
    country_dict = {'The Netherlands':'L008691','EU Total':'L008530','Belgium':'L008552', \
                    'Denmark':'L008588','Germany':'L008592','France':'L008605','Greece':'L008615', \
                    'Hungary':'L008627','Italy':'L008636','Czech Republic':'L008764', \
                    'United Kingdom':'L008776','Norway':'L008704','Canada':'L008571', \
                    'United States of America':'L008778'}
    
    for country in countries:     
        # Creates list of years and a copy
        years = []
        trimmed_years = []
        i = int(start_year)
        while i <= int(end_year):
            years.append(i)
            trimmed_years.append(i)
            i = i + 1     
               
        # Trims the dataframe down to only the required country
        country_data = cbsdata[cbsdata['Landen']==country_dict[country]]
    
        # Creates a list of asylum requests per year for that country. If there is
        # no data available, the data point is removed. 
        asylum_requests = []
        for i in years:
            try:
                asylum_requests.append(float(country_data[country_data['Perioden']==str(i)].iloc[0,2]))
            except:
                trimmed_years.remove(i)        
        
        # Plot the asylum requests over time for the country
        plt.plot(trimmed_years,asylum_requests,label=country)
    
    plt.xlabel('Years')
    xint = []
    locs, labels = plt.xticks()
    for each in locs:
        xint.append(int(each))
    plt.xticks(xint)
    plt.xlim(start_year, end_year)
    plt.ylabel('Asylum Requests (x1000)')
    plt.title('International Asylum Requests')
    plt.legend()
