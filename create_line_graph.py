import matplotlib.pyplot as plt

def create_line_graph(cbsdata,start_year,end_year,countries):
    
    # Dictionary that relates country to country code
    country_dict = {'Total Requests':'T001059','Syria':'NAT9444','Iran':'NAT9351','China':'NAT9310'}
    
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
    plt.ylabel('Asylum Requests')
    plt.title('Asylum Requests to the Netherlands')
    plt.legend()
