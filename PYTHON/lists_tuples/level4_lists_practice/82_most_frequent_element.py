numbers = [1, 3, 2, 3, 4, 3, 2]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

most_frequent = max(frequency, key=frequency.get)
print("Most frequent:", most_frequent)