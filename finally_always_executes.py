try:
    number = int(input("Enter a number: "))
    print(f"Number: {number}")
except ValueError:
    print("Error: Invalid number.")
finally:
    print("Finally block always executes.")
