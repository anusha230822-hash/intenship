try:
    first_value = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    second_value = float(input("Enter the second number: "))
    if operator == "+":
        result = first_value + second_value
    elif operator == "-":
        result = first_value - second_value
    elif operator == "*":
        result = first_value * second_value
    elif operator == "/":
        result = first_value / second_value
    else:
        raise ValueError("Unsupported operator.")
    print(f"Result: {result}")
except ValueError as error:
    print(f"Input error: {error}")
except ZeroDivisionError:
    print("Math error: Cannot divide by zero.")
except TypeError:
    print("Type error: Invalid operation values.")
