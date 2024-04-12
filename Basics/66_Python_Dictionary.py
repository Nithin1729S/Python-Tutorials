#Note:See a dictionary as a table.Every Dictionary has two parts on the left side we have the word(key) and on the right side we have value.
#Syntax: {key:value,key:value,key:value}

programming_dict={
    "Bug":"Coding error in a computer program.",
    123:"The first three numbers of the whole numbers but the key value here is in int datatype",
    "123":"The first three numbers of the whole numbers but the key value here is in string datatype"
}
#Here bug is a string and 123 is a int and "123" is a string
print(programming_dict["Bug"])     #Make sure you spell the key corectly to avoid key error.Make sure you use the correct datatype
print(programming_dict[123])
print(programming_dict["123"])

#Remember:The way to add a new element to the dictionary

programming_dict["Loop"]="The action of doing something again and again"
programming_dict["Function"]="A piece of code thea you can easily call over and over again"
print(programming_dict)

#Topic:Creating a newEmpty Dictionary
empty_dict={}

#Topic:Wipe an existing dictionary

# programming_dict=[]
# print(programming_dict)

#Topic:Edit an item in a dictionary
programming_dict["Bug"]="An error in a program that prevents the program from running as expected"
print(programming_dict)

#Topic:Loop thru a dictionary
for thing in programming_dict:
    print(thing)   #This code only prints the keys
    print(type(thing))
#PTR:Looping thru a dictionary only gives you keys and not values

for key in programming_dict:
    print(key)
    print(programming_dict[key])

#Note:Each key can only have one value








