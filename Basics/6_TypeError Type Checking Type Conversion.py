len("This function can only take strings")
#You can concatenate only a string to a string
#type() function is used to check the type of the variable
#Type Casting
a=123
print(type(a))
a=str(123)
print(type(a))

print(70 + float("100.35"))   #String got converted to float and got added to 70 mathematically
print(str(70)+str(100))       #Doesnt add mathematically but two strings get concatenated

num_char=len(input("What is your name?\n"))  #new line character inside the quotes
print(type(num_char))     #num_char is integer.So we have to cast it or convert it to  a string
print("Your name has " + str(num_char) + " characters.")



