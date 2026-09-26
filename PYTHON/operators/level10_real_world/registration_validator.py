username = "anusha"
email = "anusha@example.com"
password = "python123"
valid = len(username) >= 3 and "@" in email and len(password) >= 8
print("Registration valid:", valid)