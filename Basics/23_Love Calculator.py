print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
t = combined_name.lower().count("t")
r = combined_name.lower().count("r")
u = combined_name.lower().count("u")
e = combined_name.lower().count("e")
l = combined_name.lower().count("l")
o = combined_name.lower().count("o")
v = combined_name.lower().count("v")


true=t + r + u + e
love=l+o+v+e
score=int(str(true)+str(love))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

