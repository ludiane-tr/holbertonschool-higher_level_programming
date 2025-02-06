#!/usr/bin/python3
'''Abstract class and method'''

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
 
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def perimeter(self):
        return self.radius * 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


def shape_info(shape):
    
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
