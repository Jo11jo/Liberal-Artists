import matplotlib.pyplot as plt

def create_line_graph(cbsdata):
    years = []
    for i in range(44):
        years.append(int(cbsdata.iloc[i,1]))

    country_data = cbsdata.loc[0:43,"Nationaliteit":"TotaalAsielverzoekenEnNareizigers_1"]

    y_values = []

    for i in range(44):
        try:
            y_values.append(int(country_data.iloc[i,2]))
        except:
            y_values.append(0)

    line_graph = plt.plot(years,y_values,label="Total")
    plt.xlabel('Years')
    plt.ylabel('Asylum Requests')
    plt.title('Asylum Requests for the Netherlands')
    plt.legend()
    return line_graph