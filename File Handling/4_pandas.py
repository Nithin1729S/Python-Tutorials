import pandas

data=pandas.read_csv("weather_data.csv")
print(data)

#Get Data from columns
print(data["temp"])

data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)

# avg_temp=sum(temp_list)/len(temp_list)
# print(avg_temp)

print(data["temp"].mean())
print(data["temp"].max())


#get data from rows

print(data[data.day=='Monday'])
print(data[data.temp==data.temp.max()])

monday=data[data.day=='Monday']
print(monday.condition)


#get mondays temperature and convert it to fahrenheit

# monday_temp=data[data.day=='Monday']
# monday_temp_in_celsius= int(monday.temp)
# monday_temp_in_fah=(monday_temp_in_celsius)*(9/5)+32
# print(monday_temp_in_fah)

