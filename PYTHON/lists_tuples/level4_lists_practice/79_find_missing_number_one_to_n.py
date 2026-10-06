numbers = [1, 2, 4, 5, 6]
n = len(numbers) + 1
expected_total = n * (n + 1) // 2
actual_total = sum(numbers)

print("Missing number:", expected_total - actual_total)