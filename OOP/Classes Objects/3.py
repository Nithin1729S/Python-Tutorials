class Dog:
    def __init__(self,name):
        self.name=name
    def walk(self):
        return "*walking*"

    def speak(self):
        return "Woof!"

class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"

bobo = JackRussellTerrier("Doggie")
print(bobo.walk())
bobo.name="Bruh"
print(bobo.name)


