numbers = [10, 20, 30]

try:
    position = int(input("Enter a list index: "))
    print(f"Value: {numbers[position]}")
except IndexError:
    print("Error: The list index is out of range.")
except ValueError:
    print("Error: Enter a valid integer index.")
