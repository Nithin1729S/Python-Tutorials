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


class Programmer(Employee):
    def printprog(self):
        return f"The Programmer's name is {self.name}.Salary is {self.salary} and role is {self.role}"



harry=Employee("Harry",255,"Instrucctor")
rohan=Employee("Rohan",455,"Student")

shubham=Programmer("Shubham",555,"Programmer")
karan=Programmer("Karan",777,"Programmer")

print(karan.printprog())
print(karan.printdetails())


