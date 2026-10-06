numbers = [1, 2, 2, 3, 1, 4, 3, 3]
duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print(duplicates)