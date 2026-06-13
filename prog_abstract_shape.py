from abc import ABC,abstractmethod
class Shapes(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        return (f"{self.name}->area={self.area()},perimeter={self.perimeter()}")
class Circles(Shapes):
    def __init__(self,radius):
        super().__init__("circles")
        self.radius=radius
    def area(self):
        return 3.14159*self.radius*self.radius
    def perimeter(self):
        return 2*3.14159*self.radius
class Rectriangle(Shapes):
    def __init__(self,length,width):
        super().__init__("Rectriangle")
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
class triangle(Shapes):
    def __init__(self,a,b,c):
        super().__init__("Triangle")
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        s=self.perimeter()/2
        return (s*(s-self.a)*(s-self.b)*(self.c))**0.5
try:
    s=Shapes("nope")
except TypeError as e:
    print("cannot create shape directly:")
    print(e)
shapes=[Circles(5),Rectriangle(4,6),triangle(3,4,5)]
for i in shapes:
   print(i.describe())
