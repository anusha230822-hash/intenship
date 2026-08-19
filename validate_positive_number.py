try:
    number = float(input("Enter a positive number: "))
    if number <= 0:
        raise ValueError("Number must be positive.")
    print(f"Valid positive number: {number}")
except ValueError as error:
    print(f"Number validation error: {error}")
