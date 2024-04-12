def add(*args):
    print(args)
    return sum(args)

print(add(3,5,6))

print(add(4,5,6,7,8,1))

def calculate(n,**kwargs):
    print(kwargs)
    n+=kwargs["add"]
    n-=kwargs["multiply"]
    print(n)




calculate(2,add=3,multiply=5)


class Car:
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]

my_car=Car(make="Nissan",model="GTR")
print(my_car.model)

class Bike():
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.color=kw.get("color")
        self.seats=kw.get('seats')

my_bike=Bike(make="KTM",model="350")
print(my_bike.model)









