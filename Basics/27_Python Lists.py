#List is what we call a data structure ,which is a way to organizing and storing data in python
#To store a single pieces of data we use a simple variable (a=3 etc)
#To store grouped piece of data which are related (ex:names of all names of states of usa for this we would need a variable called states of the us and we store all the states in it)
#We would also need a order in our data.It is determined by the order in the list
"""
List:
fruits=[item1,item2]         USE SQUARE BRACKETS
We can store a string with a integer or booleans etc ie mixed data types can be used
This list will get stored in the variable
It stores a list of related variables of any type maintainning its order

"""
states_of_america=["Delaware","Pennsylvania","Ohio","FLorida"]
print(states_of_america[0])   #0 here indicates that the element if zero elements away from the start of the list
print(states_of_america[-2])   #starts counting from the end of the list from -1 as -0 is not a number
print(states_of_america[-1])   #the last element form the list

#To change a element from the list.
states_of_america[1] = "Pencilvania"
print(states_of_america[1])
print(states_of_america)
#When you print a list you get single quotes on each string indicating that its a string
#To add a element at the end of the list
states_of_america.append("Angelaland")    #doesnt return anything ie cant be equated to a variabel like len fuction.It changes the list forever

#To extend list
states_of_america.extend(["India","Pakistan","South Africa"]) #Just like append fucntion it cannoot be equated to a variable
print(states_of_america)
print(len(states_of_america))
#To get to  know about other functions use https://docs.python.org/3.11/tutorial/index.html

"""
To convert a collection of strings to a list use spilt() function
"""
names_string=input("Give all of your names separated with a comma and a space: ")
names_list= names_string.split(", ")   #removes ,and space from the string given and converts it into a list
print("The names as a list: ",names_list)
print("The names as a string: ",names_string)

