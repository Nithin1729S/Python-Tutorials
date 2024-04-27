num=int(input("Enter the number you want to check prime: "))
isPrime=True

if num==1:
    print("This is neither prime nor composite")

elif num>1:
    for i in range (2,num+1):
        if num%i==0:
            isPrime=False
            break



    if isPrime:
        print("This is a prime number")
    else:
        print("This is not a prime number")

