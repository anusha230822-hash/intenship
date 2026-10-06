first = [1, 2, 3, 4]
second = [3, 4, 5, 6]
merged_unique = []

for item in first + second:
    if item not in merged_unique:
        merged_unique.append(item)

print(merged_unique)