number = int(input("Which number do you want to check? "))


n = number % 2
if n == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
