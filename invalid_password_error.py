class InvalidPasswordError(Exception):
    pass


try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters.")
    print("Password is valid.")
except InvalidPasswordError as error:
    print(f"InvalidPasswordError: {error}")
