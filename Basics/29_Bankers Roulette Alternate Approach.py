
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
one_to_pay = random.choice(names)    #The choice function picks a random element from a list
print(f"{one_to_pay} is going to buy the meal today!")


