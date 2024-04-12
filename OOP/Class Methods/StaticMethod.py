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

    @classmethod
    def from_str(cls,string):
        params=string.split("-")
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood():
        print("This is good")


karan=Employee.from_str("Karan-500-Student")
print(karan.salary)

