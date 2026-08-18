from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    c = Circle('red', 2)
    r = Rectangle('blue', 3, 4)
    print(c.color, round(c.area(), 6))
    print(r.color, r.area())
