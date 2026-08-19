try:
    first_value = input("Enter the first value: ")
    second_value = input("Enter the second value: ")
    result = first_value / int(second_value)
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid integer input.")
except TypeError:
    print("Error: Values have incompatible types.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
