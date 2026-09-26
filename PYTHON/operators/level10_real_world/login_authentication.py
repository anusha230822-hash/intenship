entered_username, entered_password = "admin", "python123"
saved_username, saved_password = "admin", "python123"
authenticated = entered_username == saved_username and entered_password == saved_password
print("Login successful:", authenticated)