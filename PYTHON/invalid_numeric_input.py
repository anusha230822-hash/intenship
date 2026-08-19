try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print(f"Sum: {first_number + second_number}")
except ValueError:
    print("Error: Please enter valid numbers.")
