try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Age requirement satisfied.")
except ValueError as error:
    print(f"Age validation error: {error}")
