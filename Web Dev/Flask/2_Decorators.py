def outer_function():
    print("Im Outer")
    def nested_function():
        print("Im Inner")
    return nested_function
# inner_function=outer_function()
# inner_function()
outer_function()