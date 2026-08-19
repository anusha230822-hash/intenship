try:
    username = input("Enter username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    print(f"Valid username: {username}")
except ValueError as error:
    print(f"Username validation error: {error}")
