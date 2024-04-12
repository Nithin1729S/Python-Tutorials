
total=0
for number in range(2,101,2):
    total+=number
print(total)
#An alternate approach
total1=0
for number1 in range(1,101):
    if number1%2==0:
        total1+=number1
print(total1)

#To add all odd numbers from 1 to 100
total2=0
for number2 in range(1,101):
    if number2%2!=0:
        total2+=number2
print(total2)