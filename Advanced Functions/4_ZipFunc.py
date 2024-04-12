name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
zip_type=zip(name,animal)
zipped_list=list(zip(name,animal))
zipped_dict=dict(zip(name,animal))
zipped_set=set(zip(name,animal))
print(zipped_list)
print(zipped_dict)
print(zipped_set)

for (a,b) in zip(name,animal):
    print(a,b)

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for index,(name,age) in enumerate(zip(names,ages)):
    print(index,name,age)


stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,prices in zip(stocks, prices)}
print(new_dict)

