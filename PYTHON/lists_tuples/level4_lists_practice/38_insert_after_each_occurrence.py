numbers = [1, 2, 3, 2, 4, 2]
target = 2
inserted_value = 99
result = []

for number in numbers:
    result.append(number)
    if number == target:
        result.append(inserted_value)

print(result)