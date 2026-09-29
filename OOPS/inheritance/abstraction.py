from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter Length: "))
        self.breadth = int(input("Enter Breadth: "))

    def get_area(self):
        print("Area: ", self.length * self.breadth)
        
    def get_perimeter(self):
        print("Perimeter: ", 2 * (self.length + self.breadth))


class Square(Shape):
    def __init__(self):
        self.side = int(input("Enter Side: "))

    def get_area(self):
        print("Area: ", self.side ** 2)
        
    def get_perimeter(self):
        print("Perimeter: ", 4 * self.side)



rect = Rectangle()
rect.get_area()
rect.get_perimeter()


sq = Square()
sq.get_area()
sq.get_perimeter()