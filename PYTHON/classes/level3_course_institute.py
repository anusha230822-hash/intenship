class Course:
    institute_name = 'Institute of Learning'

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

if __name__ == '__main__':
    c = Course('Mathematics', '6 months')
    print(c.course_name, '-', c.duration, '-', Course.institute_name)
