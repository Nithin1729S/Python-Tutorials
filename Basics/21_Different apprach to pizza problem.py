print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if size=="S":                  #1st if
    bill+=15
elif size=="M":                #if else statement
    bill+=20
elif size=="L":
    bill+=25

if add_pepperoni=="Y":         #2nd if
    if size=="S":              #nested if
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":          #3rd if
    bill+=1

print(f"Your final bill is ${bill}")




