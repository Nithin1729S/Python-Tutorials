"""
if/else/elif                        ||                  Multiple if

if condition1:                                        if condition1:
   do A                                                  do A
elif condition2:                                     if condition2:
   do B                                                  do B
else:                                                 if condition3:
   do C                                                   do C


Here only one of                     ||              Here all three conditions are checked and if all are true all are executed
A B or C would be carried
out


"""

print("Welcome to the rollercoster")
height=int(input("What is your height in cm? "))

bill=0
if height >= 120:
    print("You can ride this rollercoast.")
    age = int(input("What is your age? "))
    if age < 12:
        bill=5
        print("Child tickets are $5")
    elif age<=18:      # Considers everyone between 12 and  18  including  12
        bill=7
        print("Youth Tickets are $7")
    else :           # Considers people above 18
        bill=12
        print("Adult tickets are $12")

    wants_photo=input("Do you want a photo taken? Y or N. ")
    if wants_photo=="Y":       #This condition needs to be asked no matter whatever there height or age is
        #Add $3 to the bill
        #bill=bill+3                      #bill value = current value +3
        bill+=3      #Same as above statement but a short hand.Adds 3 to the old value

    print(f"Your final bill is ${bill}")     #not indented to the above if  .If the input was N the control just skip the if statement and goes here

else:
    print("Sorry,You have to grow taller to ride.")
