try:
    attendance = float(input("Enter attendance percentage: "))
    required_attendance = 75
    if attendance < required_attendance:
        raise ValueError(f"Attendance must be at least {required_attendance}%.")
    print("Attendance requirement satisfied.")
except ValueError as error:
    print(f"Attendance validation error: {error}")
