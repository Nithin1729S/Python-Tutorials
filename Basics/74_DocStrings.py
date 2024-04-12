print(len("Hello"))
#If you keep your cursor of the len function which is a inbuilt function we get a description of the function on what it does.
#Same can be done with user created fucntions by using a docstring("""""")
#Docstrings allow us to write multi line comments

def format_name(f_name,l_name):
    """Take a first and last name and format it to return
    the title case version of the name"""
    if f_name=="" or l_name=="":
        return "You didn't provide valid inputs."
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name} "

format_name("niTHIn","suRESh")
