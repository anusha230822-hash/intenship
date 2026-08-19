numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter a list index: "))
    print(f"Selected value: {numbers[index]}")
except ValueError:
    print("Error: Enter an integer index.")
except IndexError:
    print("Error: Invalid list index.")
