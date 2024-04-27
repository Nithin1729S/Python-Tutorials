num=int(input("Number of required terms: "))
n1=0
n2=1
count=0
if num<=0:
    print("Invalid Input")
elif num==1:
    print("The Fibonacci Sequence: ",n1)
else:
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1