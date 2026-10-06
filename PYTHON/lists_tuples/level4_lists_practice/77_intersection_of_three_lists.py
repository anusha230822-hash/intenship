first = [1, 2, 3, 4, 5]
second = [2, 3, 4, 6]
third = [0, 2, 3, 7]
common = []

for item in first:
    if item in second and item in third and item not in common:
        common.append(item)

print(common)