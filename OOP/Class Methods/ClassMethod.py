class Employee:
    no_of_leave=0

    def __init__(self,qname,qsalary,qrole):
        self.name=qname
        self.salary=qsalary
        self.role=qrole

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is  {self.role}"

    @classmethod
    def change_leave(cls,newleave):
        cls.no_of_leave=newleave

harry=Employee("Harry",255,"Instrucctor")
rohan=Employee("Rohan",455,"Student")
harry.change_leave(34)
print(harry.no_of_leave)


