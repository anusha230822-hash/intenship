def calculate_factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Factorial requires a non-negative integer.")
    factorial = 1
    for value in range(2, number + 1):
        factorial *= value
    return factorial


try:
    number = int(input("Enter a non-negative integer: "))
    print(f"Factorial: {calculate_factorial(number)}")
except ValueError as error:
    print(f"Invalid factorial input: {error}")
