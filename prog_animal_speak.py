class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof")
class Cat(Animal):
     def speak(self):
        print(f"{self.name} says meow")
class Cow(Animal):
     def speak(self):
        print(f"{self.name} says moo")
animals = [ Dog("Buddy"),Cat("Whiskers"),Cow("Bessie"),]
for i in animals:
   i.speak()
