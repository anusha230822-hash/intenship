numbers = [1, 2, 2, 3, 1, 4, 3]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)