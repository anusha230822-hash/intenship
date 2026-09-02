class Student:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    s = Student('Alice')
    print('Student name:', s.name)
