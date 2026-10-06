numbers = [12, 7, 25, 3, 18]

if len(numbers) >= 2:
    ordered = sorted(numbers)
    print("Maximum pair sum:", ordered[-1] + ordered[-2])
else:
    print("At least two numbers are required")