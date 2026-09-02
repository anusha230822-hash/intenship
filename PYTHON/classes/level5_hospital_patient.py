class HospitalPatient:
    def __init__(self, patient_id, name, age, ailment, doctor):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment
        self.doctor = doctor

    def display(self):
        print(f"Patient: {self.name} (ID: {self.patient_id}), Age: {self.age}, Ailment: {self.ailment}, Doctor: {self.doctor}")

if __name__ == '__main__':
    p = HospitalPatient('P001', 'Anita', 45, 'Appendicitis', 'Dr. Kumar')
    p.display()
