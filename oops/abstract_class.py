# An abstract class is like a template for derived classes
# to follow. They cannot be instantiated.
# It has abstract methods (without any implementation)
# Derived classes should implement those abstract methods.
# 'abc' module in Python supports abstraction
# 'abc' - Abstract Base Classes

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    # Abstract class with two abstract methods
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * pi * self.radius

def main():
    rectangle = Rectangle(3, 5)
    print(f'Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}')

    circle = Circle(5)
    print(f'Circle Area: {circle.area()}, Perimeter: {circle.perimeter()} ')


if __name__ == '__main__':
    main()