class Patient:
    def __init__(self, name, age, disease, doctor):
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor = doctor

if __name__ == '__main__':
    p1 = Patient('P1',30,'Fever','Dr X')
    p2 = Patient('P2',45,'Diabetes','Dr Y')
    p3 = Patient('P3',60,'Hypertension','Dr Z')
    for p in (p1,p2,p3):
        print(p.name, p.age, p.disease, p.doctor)
