def divide_numbers(first_number, second_number):
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print(divide_numbers(first_number, second_number))
except ValueError:
    print("Error: Enter valid numbers.")
