numbers = [12, 7, 25, 3, 18]

if len(numbers) >= 2:
    ordered = sorted(numbers)
    print("Minimum pair sum:", ordered[0] + ordered[1])
else:
    print("At least two numbers are required")