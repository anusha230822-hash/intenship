numbers = [12, 7, 25, 18, 7, 3]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

unique_numbers.sort()
if len(unique_numbers) >= 2:
    print("Second smallest:", unique_numbers[1])
else:
    print("At least two distinct values are required")