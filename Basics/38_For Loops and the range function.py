"""
for number in range(a,b):   Instead of list we use a range here.We take each number from that range and do something from that number
    print(number)
"""
for number in range(1,11):  #Number between 1 and 10 not including 11
    print(number)
#By default the range function will step thru all the numbers from the start to the end and it will increase by 1.
#But if you want it to increase by any another number add another comma and specify that number inside range parenthesis
for number in range(1,11,2): #the range function skips two steps
    print(number)
#The range() function returns a sequence of numbers, *starting from 0 by default*, and increments by 1 (by default), and ends at a specified number.
for x in range(6):    #excludes 6
  print(x)



