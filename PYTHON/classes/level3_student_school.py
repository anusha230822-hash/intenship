class Student:
    school_name = 'Central School'

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    s = Student('Amit')
    print(s.name, '-', Student.school_name)
