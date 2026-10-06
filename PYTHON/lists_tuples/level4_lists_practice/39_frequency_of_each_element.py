items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)