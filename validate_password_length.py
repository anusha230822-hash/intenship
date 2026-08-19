try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")
    print("Password length is valid.")
except ValueError as error:
    print(f"Password validation error: {error}")
