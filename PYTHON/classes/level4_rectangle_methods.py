class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    r = Rectangle(3,4)
    print('Area:', r.area())
    print('Perimeter:', r.perimeter())
