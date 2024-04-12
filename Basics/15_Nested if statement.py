"""
if condition :
    if another condition:
         do this    For this both the condition should be true
    else:
         do this    For this condition should be true and anoter condition should be false
else:
    do this        For this the first condition should be false
"""
# A if and else statement lives inside a if statement
print("Welcome to the rollercoster")
height=int(input("What is your height in cm? "))
age=int(input("What is your age? "))
if height >= 120:
    print("You can ride this rollercoast.")
    if age<=18:
        print("Please pay $7")
    else :
        print("Please pay $12")
else:
    print("Sorry,You have to grow taller to ride.")
