student = {"name": "Anusha", "course": "Python", "age": 21}

try:
    key = input("Enter a dictionary key: ")
    print(f"Value: {student[key]}")
except KeyError:
    print("Error: The key does not exist.")
