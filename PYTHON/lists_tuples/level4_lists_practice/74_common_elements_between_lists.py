first = [1, 2, 3, 4, 5]
second = [3, 4, 5, 6, 7]
common = []

for item in first:
    if item in second and item not in common:
        common.append(item)

print(common)