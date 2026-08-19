class InvalidUsernameError(Exception):
    pass


try:
    username = input("Enter username: ").strip()
    if not username:
        raise InvalidUsernameError("Username cannot be empty.")
    print(f"Username '{username}' is valid.")
except InvalidUsernameError as error:
    print(f"InvalidUsernameError: {error}")
