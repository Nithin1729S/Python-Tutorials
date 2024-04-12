#In order to use a random module you have to import it
import random
import my_module
# Here you imported your own module

random_integer = random.randint(1,10)       #A random integer between 1 and 10(inclusive). A dot is used to acces the imported module
print(random_integer)

"""
A random module is a python module,which has to be imported to be used in the code

MODULE : If your code is very long coz you are creating something complex.What people do in that case is to spilt the code
into indivisual modules,where each module is responsible for a different bit of functionality of your code .If the program is very huge you will have a 
lot of people working on it.
Ex: While building a  car the work is spilt up to differnt people.Some people will be incharged of the engine module ,armour module,brake module,etc
put everything together you get the final car(program)

Random module is a module the python team created to make it easier for us to creat random numbers without needing to get into the complexity of all the complex math
required to generate a random number

https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

You can create your own module.
"""

print(my_module.pi)     # . is used to acces the module

#To generate a random floating point number
random_float = random.random()     #read the description of the function .It generated a random number between 0 and 1 excluding 1
print(random_float)
print(random_float*5)            #gives a random floating point number between 0 and 5 excluding 5

love_score=random.randint(1,100)
print(f"Your love score is {love_score}")
