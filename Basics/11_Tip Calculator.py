print('Welcome to the tip calculator!')
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
spilt=int(input("How many people to split the bill? "))
total=bill+bill*(tip/100)
#total=bill*(1 + tip/100)    Alternate Way
pay=round(total/spilt,2)
print(f"Each person should pay: ${pay}")
