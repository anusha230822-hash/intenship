try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"Square: {number ** 2}")
