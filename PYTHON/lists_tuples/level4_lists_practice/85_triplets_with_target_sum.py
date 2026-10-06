numbers = [1, 2, -2, 0, -1, 3]
target = 0
triplets = []

for first_index in range(len(numbers)):
    for second_index in range(first_index + 1, len(numbers)):
        for third_index in range(second_index + 1, len(numbers)):
            if numbers[first_index] + numbers[second_index] + numbers[third_index] == target:
                triplets.append((numbers[first_index], numbers[second_index], numbers[third_index]))

print(triplets)