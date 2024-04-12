travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited,number_of_times,cities_visited):
    new_country={}     #Since the list contains dictionaries we have to append a dict to it.
    new_country["country"]=country_visited
    new_country["visits"]=number_of_times
    new_country["cities"]=cities_visited
    travel_log.append(new_country)

#Calling the function
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])    #This would print steak.
#starter main and dessert are the keywords of the dict order
#1 and 2 are the keyword of the dict main here
#0 is the index of the list 2
