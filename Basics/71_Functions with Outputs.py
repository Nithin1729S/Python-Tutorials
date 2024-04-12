        #Topic:Normal Function   def  my_fucntion():
                                 #do this
                                 #then do this
                                 #finally do this

#Topic:FUnctions with inputs    def my_functions(parmeters here):
                                #do this with parameter
                                #then do this
                                #finally do this

#Topic:Functions with outputs   def my_function():
                                #result=3*2
                                #return result This result will replace my_function():    line of code, where this function was called

def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"    #here the formatted string is the output
#everything which comes after the return function replaces the function call statement
#if you write anything after return fucntion it will not be executed as return tells the computer that it is the end of the function and you should now exit the function
#you can have multiple return keyword within the same funtion ,you can also have empty return keywords

#Note:Difference between title() and capitalize()
# str = "geeks for geeks"
# str.title() will return Geeks For Geeks
# str.capitalize() will return Geeks for geeks

formated_sring=format_name("angela","yU")
print(formated_sring)

output=len("Angela") #len is a inbuilt function and we used to use it as a function which reutrned values


