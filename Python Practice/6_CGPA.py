credits=[]
weighted_grade_point=[]

while True:
    lst=list(input("Enter the CGPA of a subject and it's credits seperated by a whitespace: ").split())
    if "q" in lst:
        break
    credits.append(int(lst[1]))
    weighted_grade_point.append(int(lst[0])*int(lst[1]))

cgpa=sum(weighted_grade_point)/sum(credits)

print(cgpa)