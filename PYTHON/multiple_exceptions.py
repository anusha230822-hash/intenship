try:
    numbers = [10, 20, 30]
    index = int(input("Enter an index: "))
    divisor = int(input("Enter a divisor: "))
    print(f"Result: {numbers[index] / divisor}")
except ValueError:
    print("Error: Please enter integers only.")
except IndexError:
    print("Error: The list index is out of range.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
