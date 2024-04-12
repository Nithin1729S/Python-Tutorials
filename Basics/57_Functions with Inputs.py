def greet():
    print("Hi there Hello Angela")
    print("How do you do Ryan George?")
    print("How are you Johan?")

greet()

# Topic:Function that allows for input

def greet_with_name(name):
    print(f"Hi there Hello {name} ")
    print(f"How do you do {name}?")
    print(f"How are you {name}?")

greet_with_name("Angela")

#Syntax:   def my function(something):
           #Do this with something
           #then do this
           #finally do this

#We are creating a new variable called something and we are setting  it to be equal to this piece of data (name we wrote while calling the function)
#here something is called parameter and Angela is called argument
#Argument is the actual piece of data which will be passed over to the function when its being called,whereas parameter is the name of the data
#and we use the parameter inside the function to refer to it and to do things

