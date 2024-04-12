from calculator_art import logo
print(logo)

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

def calculator():
    num1=float(input("What's the first number? : "))
    should_continue=True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation from above: ")
        num2=float(input("What's the next number? : "))
        calculator_function = operations[operation_symbol]
        answer=calculator_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice=input(f"Type 'Y' if you want to continue working with {answer} if not type 'N' to start a new calculation").lower()
        if choice=="n":
            should_continue=False
            calculator()
        else:
             num1=answer


calculator()





