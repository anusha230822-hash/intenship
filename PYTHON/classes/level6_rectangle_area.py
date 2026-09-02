class Rectangle:
    def area(self, length, width):
        return length * width

if __name__ == '__main__':
    r = Rectangle()
    print('Area:', r.area(5, 4))
