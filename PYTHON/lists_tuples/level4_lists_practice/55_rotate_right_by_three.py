items = [1, 2, 3, 4, 5, 6]
positions = 3 % len(items)
rotated = items[-positions:] + items[:-positions]

print(rotated)