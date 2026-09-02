from abc import ABC, abstractmethod


class Dog:
    def sound(self): return "Dog barks"
class Cat:
    def sound(self): return "Cat meows"
class Car:
    def start(self): return "Car starts"
class Bike:
    def start(self): return "Bike starts"
class Bus:
    def start(self): return "Bus starts"
class Rectangle:
    def area(self): return 20 * 10
class Circle:
    def area(self): return 3.14 * 5 * 5
class Animal:
    def sound(self): return "Animal sound"
class Cow(Animal):
    def sound(self): return "Cow moos"
class Duck:
    def walk(self): return "Duck walks"
class Printer:
    def print(self): return "Printer prints"
class PDFPrinter:
    def print(self): return "PDF printer prints"
class Payment:
    def pay(self): return "Payment completed"
class UPI(Payment):
    def pay(self): return "UPI payment completed"
class CreditCard(Payment):
    def pay(self): return "Credit card payment completed"
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)
    def __repr__(self): return f"Point({self.x}, {self.y})"
class Money:
    def __init__(self, amount): self.amount = amount
    def __add__(self, other): return Money(self.amount + other.amount)
    def __repr__(self): return f"Money({self.amount})"
class AbstractShape(ABC):
    @abstractmethod
    def area(self): pass
class AbstractCircle(AbstractShape):
    def area(self): return 78.5


def use_method(objects, method):
    return [getattr(obj, method)() for obj in objects]


def run(level, question):
    basic = [use_method([Dog(), Cat()], "sound"), use_method([Car(), Bike(), Bus()], "start"), [Rectangle().area(), Circle().area()], ["Student details", "Teacher details"], ["Email sent", "SMS sent"], ["Developer works", "Tester works", "Manager works"], ["PDF opened", "Word opened", "Excel opened"], [UPI().pay(), CreditCard().pay(), "Cash payment completed"], ["Bird flies", "Dog walks", "Fish swims"], ["Android features", "iPhone features", "WindowsPhone features"]]
    override = [["Animal sound", Dog().sound(), Cat().sound(), Cow().sound()], [Car().start(), Bike().start(), Bus().start()], ["Manager salary", "Developer salary"], [Rectangle().area(), Circle().area(), "Triangle area"], [UPI().pay(), CreditCard().pay(), "Net banking payment"], ["Email sent", "SMS sent", "WhatsApp sent"], ["Savings interest", "Current interest"], ["Student role", "Teacher role", "Doctor role"], ["Laptop process", "Desktop process", "Server process"], ["Pizza prepared", "Burger prepared", "Biryani prepared"]]
    duck = [use_method([Duck(), Dog()], "walk"), use_method([Printer(), PDFPrinter()], "print"), use_method([Car(), Bike()], "start"), ["Email sent", "SMS sent"], [UPI().pay(), CreditCard().pay()], use_method([Dog(), Cat(), Cow()], "sound"), ["Excel report", "PDF report"], ["Online course", "Offline course"], ["Android call", "iPhone call"], ["Debit card paid", "Credit card paid"]]
    functions = [[Rectangle().area(), Circle().area()], [UPI().pay(), CreditCard().pay()], ["Email sent", "SMS sent"], [Car().start(), Bike().start()], ["Developer works", "Manager works"], ["PDF read", "CSV read"], ["MySQL connected", "SQLite connected"], ["PDF report", "Excel report"], ["Road delivery", "Air delivery"], ["Password login", "OTP login"]]
    operators = [Point(1, 2) + Point(3, 4), "Distance(15 km)", "Book A is more expensive", "Student A has higher marks", "Product total price", Money(100) + Money(50), "Rectangles have equal area", "Employee A earns more", "Temperature A is higher", "Combined cart items"]
    advanced = [["Circle area", "Rectangle area", "Triangle area"], [UPI().pay(), CreditCard().pay(), "Net banking"], ["Manager salary", "Developer salary"], ["Email", "SMS", "WhatsApp"], ["Car start/stop", "Bike start/stop", "Bus start/stop"], ["Database connect/insert/close"], ["File read/write"], ["Password/OTP/Biometric login"], ["Delivery charge calculated"], ["Tax calculated"]]
    projects = ["Payment Processing System", "Shape Calculator", "Employee Salary System", "Notification System", "Vehicle Management", "Food Ordering", "Banking Interest System", "Online Shopping Payments", "File Management", "Complete OOP Polymorphism Project"]
    data = {1: basic, 2: override, 3: duck, 4: functions, 5: operators, 6: advanced, 7: projects}
    print(data[level][question - 1])
