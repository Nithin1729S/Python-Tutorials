
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list=[]  #for this instead of an empty string we start with a empty list,as there is no easy way to shuffle a string
for i in range(nr_letters):
    letters_random=random.choice(letters)
    password_list.append(letters_random)
for i in range(nr_symbols):
    symbols_random=random.choice(symbols)
    password_list.append(symbols_random)
for i in range(nr_numbers):
    numbers_random=random.choice(numbers)
    password_list.append(numbers_random)
random.shuffle(password_list)     #shuffles the list and doesnt return anything so you cant equate it to a variable..Just like append
#to return convert the list to a string
password=""
for i in password_list:
    password+=i
print("Your password is " + password)




