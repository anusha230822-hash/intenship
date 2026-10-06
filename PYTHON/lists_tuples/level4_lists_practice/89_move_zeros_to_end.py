numbers = [0, 1, 0, 3, 12, 0, 5]
non_zero_numbers = [number for number in numbers if number != 0]
zero_count = len(numbers) - len(non_zero_numbers)
result = non_zero_numbers + [0] * zero_count

print(result)