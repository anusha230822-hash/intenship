student = {"name": "Anusha", "age": 21}

try:
    key = input("Enter a dictionary key: ")
    if not isinstance(key, str):
        raise TypeError("Dictionary key must be a string.")
    print(f"Value: {student[key]}")
except KeyError:
    print("Error: The dictionary key was not found.")
except TypeError as error:
    print(f"Error: {error}")
