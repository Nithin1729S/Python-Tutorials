import random

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9''!', '#', '$', '%',
           '&', '(', ')', '*', '+']

print("Welcome to Password Generator")
number = int(input("Enter the number of characters you need in the password \n"))

password_list = []
for i in range(number):
    random_char=random.choice(char)
    password_list.append(random_char)
print(password_list)
print(type(password_list))

password=""
for i in password_list:
    password+=i
print(password)



