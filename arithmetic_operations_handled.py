try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print(f"Addition: {first_number + second_number}")
    print(f"Subtraction: {first_number - second_number}")
    print(f"Multiplication: {first_number * second_number}")
    print(f"Division: {first_number / second_number}")
except ValueError:
    print("Error: Enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
