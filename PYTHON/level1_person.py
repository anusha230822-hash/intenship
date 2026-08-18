from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        return "I am a student"

class Teacher(Person):
    def role(self):
        return "I am a teacher"

if __name__ == "__main__":
    print(Student().role())
    print(Teacher().role())
