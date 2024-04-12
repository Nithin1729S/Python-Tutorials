class A:
    def __init__(self):
        self.name="Karan"


class B(A):
    pass

class C:
    pass

a=A()
b=B()
print(b.name)

print(a.name)