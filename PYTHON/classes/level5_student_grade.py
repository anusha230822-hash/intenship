class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list

    def average(self):
        return sum(self.marks)/len(self.marks) if self.marks else 0

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        if avg >= 80:
            return 'B'
        if avg >= 70:
            return 'C'
        if avg >= 60:
            return 'D'
        return 'F'

if __name__ == '__main__':
    s = Student('Maya', [92, 88, 95])
    print('Average:', s.average())
    print('Grade:', s.grade())
