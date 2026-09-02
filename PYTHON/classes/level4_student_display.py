class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"

if __name__ == '__main__':
    s = Student('Asha', 19, 'Biology')
    print(s.display())
