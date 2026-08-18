from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

if __name__ == '__main__':
    shapes = [Circle(2), Rectangle(3,4)]
    for s in shapes:
        print(type(s).__name__, s.area())
