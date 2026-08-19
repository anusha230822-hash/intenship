class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.users = {"anusha": "python123"}

    def login(self, username, password):
        if username not in self.users:
            raise InvalidUsernameError("Username does not exist.")
        if self.users[username] != password:
            raise InvalidPasswordError("Incorrect password.")
        return "Login successful."


try:
    login_system = LoginSystem()
    print(login_system.login("anusha", "wrong"))
except (InvalidUsernameError, InvalidPasswordError) as error:
    print(f"Login error: {error}")
