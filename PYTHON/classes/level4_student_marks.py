class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return sum(self.marks)/len(self.marks) if self.marks else 0

if __name__ == '__main__':
    s = Student('Rita', [80, 90, 85])
    print('Total:', s.total_marks())
    print('Average:', s.average_marks())
