"""
if condition1 and condition 2 and condition3:
     do this
else:
     do this
"""

#and ,or ,not are the three logical operators
# And : All the conditions should be true, for the entire line of code to be true
#Or : Any one of the conditions should be true, for the entire codd to be true
#not:reverses a condition.

print("Welcome to the rollercoster")
height=int(input("What is your height in cm? "))

bill=0
if height >= 120:
    print("You can ride this rollercoast.")
    age = int(input("What is your age? "))
    if age < 12:
        bill=5
        print("Child tickets are $5")
    elif age<=18:
        bill=7
        print("Youth Tickets are $7")
    elif age>=45 and age<= 55:
        print("Everything is going to be okay. Have a free ride on us")
    else :
        bill=12
        print("Adult tickets are $12")

    wants_photo=input("Do you want a photo taken? Y or N. ")
    if wants_photo=="Y":

        bill+=3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry,You have to grow taller to ride.")
