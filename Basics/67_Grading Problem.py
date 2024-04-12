student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {} #Note:We use flower braces for creating an emoty dictionary

# TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    score = student_scores[name]
    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)
print(student_grades["Harry"])
print(student_grades["Hermione"])
