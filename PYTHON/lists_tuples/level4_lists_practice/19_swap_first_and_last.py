items = [10, 20, 30, 40]

if len(items) >= 2:
    items[0], items[-1] = items[-1], items[0]

print(items)