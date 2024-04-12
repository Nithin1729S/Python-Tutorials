#Function which allows multiple inputs

def greet_with(name,location):     #name and location here are parameters
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Angela","England")      #Angela and England are the arguments.Here this two arguents are called `Postitional arguments
#In positional arguments the paramete is assigned the aragument value based on the position of the arguments.Here the order of the arguments is very important

#Note:We can use Keyword Arguments to be more specific as to which parameter gets what argument asigned.
#my_function=(a=1,b=2,c=7)    Here a b c are parameters and 1 2 7 are arguments assigned to them
#Here the order of the arguments doesnt matter

def greet_With(name,location):
     print(f"Hello {name}")
     print(f"What is it like in {location}")

greet_With(location="England",name="Angela")      #Remember:Keyword argument is used here

















