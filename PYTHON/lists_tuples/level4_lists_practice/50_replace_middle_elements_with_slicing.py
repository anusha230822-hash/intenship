items = [10, 20, 30, 40, 50, 60]
middle_start = len(items) // 2 - 1
items[middle_start:middle_start + 2] = [99, 100]

print(items)