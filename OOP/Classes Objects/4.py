class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance variable in class A"
class B(A):
    classvar1="I am in class B"

a=A()
b=B()

print(b.classvar1)
print(b.classvar1)