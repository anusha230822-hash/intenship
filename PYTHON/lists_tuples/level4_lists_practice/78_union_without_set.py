first = [1, 2, 3, 4]
second = [3, 4, 5, 6]
union = []

for item in first + second:
    if item not in union:
        union.append(item)

print(union)