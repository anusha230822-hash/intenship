numbers = [1, 3, 2, 3, 4, 3, 2]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

least_frequent = min(frequency, key=frequency.get)
print("Least frequent:", least_frequent)