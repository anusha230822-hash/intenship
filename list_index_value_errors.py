numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter a list index: "))
    print(f"Selected value: {numbers[index]}")
except ValueError:
    print("Error: The index must be an integer.")
except IndexError:
    print("Error: The index is outside the list range.")
