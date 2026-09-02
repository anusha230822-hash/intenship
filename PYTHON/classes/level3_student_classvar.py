class Student:
    college_name = 'ABC College'

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    s1 = Student('Alice')
    s2 = Student('Bob')
    s3 = Student('Carol')
    for s in (s1,s2,s3):
        print(s.name, '-', Student.college_name)
