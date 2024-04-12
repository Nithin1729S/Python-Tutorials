def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide}

num1=int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol=input("Pick an operation from the line above: ")

num2=int(input("What's the second number?: "))
calculation_function=operations[operation_symbol]   #Accessing the dictionary and creating a new function using it
first_answer=calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol=input("Pick another operation: ")
num3=int(input("What's the next number?: "))
calculation_function=operations[operation_symbol]
second_answer=calculation_function(calculation_function(num1,num2),num3)  #You are able to do this becoz you have used return function and not print function

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")



