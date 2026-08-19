class InvalidPasswordError(Exception):
    pass


def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters.")
    if not any(character.isdigit() for character in password):
        raise InvalidPasswordError("Password must contain at least one digit.")
    return True


try:
    password = input("Enter password: ")
    validate_password(password)
    print("Password is valid.")
except InvalidPasswordError as error:
    print(f"Password error: {error}")
