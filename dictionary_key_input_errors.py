student = {"name": "Anusha", "course": "Python", "age": 21}

try:
    key = input("Enter a dictionary key: ").strip()
    if not key:
        raise ValueError("The key cannot be empty.")
    print(f"Value: {student[key]}")
except ValueError as error:
    print(f"Input error: {error}")
except KeyError:
    print("Error: The key does not exist.")
except TypeError:
    print("Error: Invalid key type.")
