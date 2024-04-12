
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

size=len(names)-1
choice=random.randint(0,size)
print(f"{names[choice]} is going to buy the meal today!")


