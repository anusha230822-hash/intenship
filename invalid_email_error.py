class InvalidEmailError(Exception):
    pass


def validate_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError("Enter a valid email address.")


try:
    email = input("Enter email address: ").strip()
    validate_email(email)
    print("Email address is valid.")
except InvalidEmailError as error:
    print(f"InvalidEmailError: {error}")
