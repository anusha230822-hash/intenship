text = input("Enter an integer value: ")

try:
    number = int(text)
    print(f"Converted integer: {number}")
except ValueError:
    print("Error: The string cannot be converted to an integer.")
