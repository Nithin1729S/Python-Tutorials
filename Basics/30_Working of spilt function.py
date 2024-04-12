import random
names_strings="Nithin is a good boy"
print(type(names_strings))
names_list=names_strings.split()
print(type(names_list))
print(names_list)

names_strings="Nithin, is, a, good, boy"
print(type(names_strings))
names_list=names_strings.split()
print(type(names_list))
print(names_list)

names_strings="Nithin, is, a, good, boy"
print(type(names_strings))
names_list=names_strings.split(", ")
print(type(names_list))
print(names_list)

#len function gives the number of characters in a string and numbet of elements in a list
#choice() function picks a random item from a list print(random.choice(a))