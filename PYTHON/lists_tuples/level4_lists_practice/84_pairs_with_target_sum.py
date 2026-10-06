numbers = [2, 4, 3, 5, 7, 8, -1]
target = 7
pairs = []

for first_index in range(len(numbers)):
    for second_index in range(first_index + 1, len(numbers)):
        if numbers[first_index] + numbers[second_index] == target:
            pairs.append((numbers[first_index], numbers[second_index]))

print(pairs)