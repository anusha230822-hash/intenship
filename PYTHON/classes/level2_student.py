class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

if __name__ == '__main__':
    s1 = Student('Alice', 20, 'CS')
    s2 = Student('Bob', 21, 'Math')
    s3 = Student('Carol', 19, 'Physics')
    for s in (s1, s2, s3):
        print(s.name, s.age, s.course)
