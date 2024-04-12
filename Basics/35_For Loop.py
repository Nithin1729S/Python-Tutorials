"""
for items in  list_of_items:
     Do something to "each item
"""
fruits=["Apple","Peach","Pear"]
for fruit in fruits:             #Remember:The datatype of fruit here is string
    print(fruit)
    print(fruit+" Pie")   #string concatenation
print(fruit)   #prints pear as thats the last value the variable fruit obtained
#This code is taking the elements from the list fruits and assigning a variable name fruit to each of them.
#The first time it runs fruit is equal to apple ,the second time it runs fruit is equal to peach and so on it keeps changing
#A loop helps us to execute a line of code multiple times.Here we are executing the print 3 times,
#for loop can whole block of code multiple times not only one statement
#indented code are inside the for loop
#for loop is gonna run as many times as the number of elements in the list
#Try to keep the variable name in the for loop singular of the list name

"""
To convert a collection of strings to list
"""
string1=input("Write ten random numbers \n")
list1=string1.split()  #split function is used to convert a string to list
print(string1)
print(type(string1))
print(list1)
print(type(list1))
#Now the list contains a lot of string characters to typecast all the elements of the list to int
for i in range(len(list1)):     #Remember:The datatype of i here is integer
    list1[i]=int(list1[i])
print(list1)
print(type(list1))

string1="Hello World"
list1=string1.split()
print(string1)
print(list1)

#Note:Using for loop with 'in'
#Since we know that for loop iterates over each element of a list.We can use this to check if a particlar element is present in a list
squares = [1, 4, 9, 16]
sum1 = 0
for num in squares:      #Remember:here num takes the values of each element of the list
    sum1 += num
print(sum1)  #Prints sum of all elements in the list

list9 = ['larry', 'curly', 'moe']
if 'curly' in list9:
    print('yay')





