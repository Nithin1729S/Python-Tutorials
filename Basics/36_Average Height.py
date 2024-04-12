
student_heights = input("Input a list of student heights ").split()
for n in range(len(student_heights)):
  student_heights[n] = int(student_heights[n])
#This typecasts all the string elements in the list to integers

total_height=0
for height in student_heights:
    total_height+=height
print(total_height)
#you could use total_height=sum(student_heights)   This gives sum of all the elements in the list

no_of_students=0
for item in student_heights:
    no_of_students+=1
print(no_of_students)
#you could use no_of_students=len(student_heights)

average=round(total_height/no_of_students)
print(average)


