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



def calculator():  #Remember:this is a recursive function which calls itself(ie calling a function within its own definition) and takes no inputs and has no outputs.Once the control gets here all the previous calculations will be forgotten
    num1 = int(input("What's the first number?: "))
    should_continue = True  # This is called a flag

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]  # Accessing the dictionary and creating a new function using it.This function will change from add subtract multiply etc according to the key
        answer = calculation_function(num1, num2)    #This output will be reused in other parts of the code

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculation with {answer},or type 'n' to start a new calculation.:").lower()
        if choice == "n":
            should_continue = False
            calculator()  # Note:now this whole calculator function will be called again
        else:
            num1 = answer

calculator()    #This would start the program




