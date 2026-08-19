try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    print(f"Result: {numerator / denominator}")
except ValueError:
    print("Error: Enter valid numeric values.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
