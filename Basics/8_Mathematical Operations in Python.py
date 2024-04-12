 # + sign is used to concatenate to strings and also to mathematically add two numbers
 #    - for subtraction
 #    * for multiplication
 #    / for division .Division always outputs a floating point number regardless of the remainder
 #    ** used to raise a number to power
 #    // floor division.Divides two numbers and gives a integer chops of the remainder .ie estimation wont be always right
 #    % gives the remainder of the division
 #    PEMDAS is followed

"""" 
         Parentheses
         Exponents
         Multiplication
         Division
         Addition
         Subtraction
"""

print(type(6/2))
print(type(6//2))
print(6//2)
print(6/4)
print(6//4)
print(8/3)
print(8//3)
print(2**4)
print(3*3+3/3-3)
#we can use the parantheses to prioritize some opereations
print(3*(3+3)/3-3)   #the one inside the parenthesis has the highest priority now
print(5*2**10)