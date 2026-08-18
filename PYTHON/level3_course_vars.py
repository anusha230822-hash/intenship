from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass

class OnlineCourse(Course):
    def start(self):
        return f"Starting online course {self.course_name} for {self.duration}"

class OfflineCourse(Course):
    def start(self):
        return f"Starting offline course {self.course_name} for {self.duration}"

if __name__ == '__main__':
    o = OnlineCourse('Math', '6 weeks')
    off = OfflineCourse('Physics', '8 weeks')
    print(o.start())
    print(off.start())
