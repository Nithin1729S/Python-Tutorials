height=float(input("Enter your height in metres: "))
weight=float(input("Enter your weight in Kgs: "))
bmi=weight/(height**2)
if height>3:
    raise ValueError("Invalid Height")
print(bmi)
