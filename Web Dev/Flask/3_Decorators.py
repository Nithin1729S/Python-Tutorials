

import time
def delay_decorator(func):
    def wrapper_func():
        time.sleep(10)
        func()
    return wrapper_func()








def say_hello():
    print("Hello")








@delay_decorator
def greetings():
    print("Hello")



# say_hello()
# # greetings()


