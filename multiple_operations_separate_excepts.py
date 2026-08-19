numbers = [10, 20, 30]
student = {"name": "Anusha"}

try:
    index = int(input("Enter a list index: "))
    divisor = int(input("Enter a divisor: "))
    key = input("Enter a dictionary key: ")
    print(f"List value: {numbers[index]}")
    print(f"Division result: {100 / divisor}")
    print(f"Dictionary value: {student[key]}")
except ValueError:
    print("ValueError: Enter valid integer values.")
except IndexError:
    print("IndexError: The list index is invalid.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
except KeyError:
    print("KeyError: The dictionary key does not exist.")
