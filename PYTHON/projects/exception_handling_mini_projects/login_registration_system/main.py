class InvalidUsernameError(Exception):
    pass


class WeakPasswordError(Exception):
    pass


class DuplicateUsernameError(Exception):
    pass


class InvalidLoginError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if not username.strip():
            raise InvalidUsernameError("Username cannot be empty.")
        if len(password) < 8:
            raise WeakPasswordError("Password must contain at least 8 characters.")
        if username in self.users:
            raise DuplicateUsernameError("Username already exists.")
        self.users[username] = password

    def login(self, username, password):
        if self.users.get(username) != password:
            raise InvalidLoginError("Invalid username or password.")
        return "Login successful."


try:
    login = LoginSystem()
    login.register("anusha", "python123")
    print(login.login("anusha", "python123"))
except (InvalidUsernameError, WeakPasswordError, DuplicateUsernameError, InvalidLoginError) as error:
    print(f"Login error: {error}")
