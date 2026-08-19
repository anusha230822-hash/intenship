try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise ValueError("Number cannot be negative.")
    print(f"Valid number: {number}")
except ValueError as error:
    print(f"Validation error: {error}")
