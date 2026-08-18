from abc import ABC, abstractmethod

class UniversityCourse(ABC):
    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass

class EngineeringCourse(UniversityCourse):
    def start_course(self):
        return "Engineering course started"
    def get_duration(self):
        return "4 years"

class MedicalCourse(UniversityCourse):
    def start_course(self):
        return "Medical course started"
    def get_duration(self):
        return "5 years"

class ManagementCourse(UniversityCourse):
    def start_course(self):
        return "Management course started"
    def get_duration(self):
        return "2 years"

if __name__ == '__main__':
    courses = [EngineeringCourse(), MedicalCourse(), ManagementCourse()]
    for c in courses:
        print(type(c).__name__, '-', c.start_course(), '/', c.get_duration())
