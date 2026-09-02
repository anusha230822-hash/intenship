class Student:
    def __init__(self, name):
        self.name = name

    def grade_from_marks(self, marks):
        avg = sum(marks)/len(marks) if marks else 0
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
    s = Student('Ria')
    print('Grade:', s.grade_from_marks([85, 78, 92]))
