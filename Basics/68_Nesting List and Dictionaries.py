#Syntax: {Key:[List1],Key2:{dict}

#Topic:Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Topic:Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Topic:Nesting Dictionary in a Dictionary

travel_log1 = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log2 = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(travel_log)
print(travel_log1)
print(travel_log2)
print(type(travel_log))
print(type(travel_log1))
print(type(travel_log2))

#Note:In list we access list by using indices but in dictionary we use key to access it.We also use curly
# braces in dictionary unlike square brackets in list.But to access a element from the lists or dict we only use square braces
