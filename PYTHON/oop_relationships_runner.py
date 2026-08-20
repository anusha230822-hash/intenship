class Vehicle:
    def move(self): return "Vehicle moves"
class Car(Vehicle):
    def move(self): return "Car drives"
class Bike(Vehicle): pass
class Bus(Vehicle): pass
class Animal:
    def sound(self): return "Animal sound"
class Dog(Animal):
    def sound(self): return "Dog barks"
class Cat(Animal):
    def sound(self): return "Cat meows"
class Person:
    def __init__(self, name): self.name = name
class Student(Person): pass
class Teacher(Person): pass
class Employee:
    def role(self): return "Employee"
class Manager(Employee):
    def role(self): return "Manager"
class Developer(Employee):
    def role(self): return "Developer"
class Tester(Employee):
    def role(self): return "Tester"
class Shape:
    def area(self): return 0
class Rectangle(Shape):
    def __init__(self, length, width): self.length, self.width = length, width
    def area(self): return self.length * self.width
class Engine:
    def start(self): return "Engine started"
class CarWithEngine:
    def __init__(self): self.engine = Engine()
class Printer:
    def print_text(self, text): return f"Printed: {text}"
class StudentWithPrinter:
    def show(self): return Printer().print_text("Student details")


def run(level, question):
    inheritance = [
        "Car IS-A Vehicle", "Dog IS-A Animal", "Student IS-A Person", "Manager IS-A Employee", "Rectangle IS-A Shape",
        [Car().move(), Bike().move(), Bus().move()], [Dog().sound(), Cat().sound()], "Student and Teacher inherit Person",
        "SavingsAccount and CurrentAccount inherit BankAccount", [Developer().role(), Tester().role(), Manager().role()],
    ]
    composition = [
        "Car HAS-A Engine", "Computer HAS-A CPU", "House HAS-A Rooms", "Library HAS-A Books", "College HAS-A Students",
        "Department HAS-A Employees", "School HAS-A Teachers and Students", "Company HAS-A Departments", "ShoppingCart HAS-A Products", "Hospital HAS-A Doctors and Patients",
    ]
    uses = [
        StudentWithPrinter().show(), "BankAccount USES-A PaymentService", "ShoppingCart USES-A PaymentGateway", "Employee USES-A ReportGenerator", "Student USES-A NotificationService",
        "Order USES-A EmailService", "Library USES-A SearchService", "Hospital USES-A BillingService", "FoodOrder USES-A DeliveryService", "Course USES-A CertificateGenerator",
    ]
    identified = ["Dog IS-A Animal", "Car HAS-A Engine", "Student USES-A Printer", "Manager IS-A Employee", "Library HAS-A Books", "ShoppingCart USES-A PaymentGateway", "Laptop HAS-A Keyboard", "Teacher IS-A Person", "Order USES-A PaymentService", "Company HAS-A Employees"]
    combined = [
        "Car IS-A Vehicle and HAS-A Engine", "Student IS-A Person and HAS-A Course", "Developer IS-A Employee and HAS-A Laptop", "Library HAS-A Books and USES-A SearchService", "ShoppingCart HAS-A Products and USES-A PaymentGateway",
        "Hospital HAS-A Doctors/Patients and USES-A BillingService", "Company HAS-A Departments/Employees and USES-A PayrollService", "School HAS-A Teachers/Students and USES-A NotificationService", "OnlineOrder HAS-A Products and USES-A Payment/Delivery", "University IS-A Institution, HAS-A Departments, USES-A ExaminationService",
    ]
    projects = ["Library Management", "Banking System", "Hospital Management", "E-Commerce", "School Management", "Vehicle Rental", "Food Delivery", "Company Management", "Online Learning", "Complete IS-A/HAS-A/USES-A OOP Project"]
    data = {1: inheritance, 2: composition, 3: uses, 4: identified, 5: combined, 6: projects}
    print(data[level][question - 1])
