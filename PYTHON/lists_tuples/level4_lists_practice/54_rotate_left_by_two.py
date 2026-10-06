items = [1, 2, 3, 4, 5, 6]
positions = 2 % len(items)
rotated = items[positions:] + items[:positions]

print(rotated)