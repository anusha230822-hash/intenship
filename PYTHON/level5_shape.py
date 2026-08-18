from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        return "This is a shape"

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
    c = Circle(2)
    r = Rectangle(3,4)
    print(c.area(), c.display_shape())
    print(r.area(), r.display_shape())
