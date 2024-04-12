
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(args[0],args[1],args[2])}")
    return wrapper



@logging_decorator
def multiply(a,b,c):
    return a*b*c


multiply(1,3,4,5)