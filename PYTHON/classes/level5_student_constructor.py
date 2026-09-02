class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks  # list of numbers

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

    def average(self):
        return sum(self.marks)/len(self.marks) if self.marks else 0

if __name__ == '__main__':
    s = Student('Asha', 19, 'Biology', [78, 82, 90])
    s.display()
    print('Average:', s.average())
