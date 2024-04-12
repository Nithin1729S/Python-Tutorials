"""
if condition 1:
      do A
elif condition 2:     If condition 1 is not true.There can be as many elif as possible.Elif means else if
       do B
else :
       do this       If all the above conditions are false

Here we check only one condition even if there are other conditions.If you had to check  multiple  conditiions even if the
previous condition was true than we use multiple if in succestion
"""






print("Welcome to the rollercoster")
height=int(input("What is your height in cm? "))
age=int(input("What is your age? "))
if height >= 120:
    print("You can ride this rollercoast.")
    if age < 12:
        print("Please pay $5")
    elif age<=18:      # Considers everyone between 12 and  18  including  12
        print("Please pay $7")
    else :           # Considers people above 18
        print("Please pay $12")
else:
    print("Sorry,You have to grow taller to ride.")
