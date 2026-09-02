class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

if __name__ == '__main__':
    t1 = Teacher('Mr A','Math',10)
    t2 = Teacher('Ms B','Physics',8)
    t3 = Teacher('Mrs C','Chemistry',12)
    for t in (t1,t2,t3):
        print(t.name, t.subject, t.experience)
