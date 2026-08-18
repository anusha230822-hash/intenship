from abc import ABC, abstractmethod

class HospitalEmployee(ABC):
    @abstractmethod
    def perform_duty(self):
        pass

class Doctor(HospitalEmployee):
    def perform_duty(self):
        return "Diagnose and treat patients"

class Nurse(HospitalEmployee):
    def perform_duty(self):
        return "Assist doctor and care for patients"

class Pharmacist(HospitalEmployee):
    def perform_duty(self):
        return "Dispense medications"

if __name__ == '__main__':
    staff = [Doctor(), Nurse(), Pharmacist()]
    for s in staff:
        print(type(s).__name__, '-', s.perform_duty())
