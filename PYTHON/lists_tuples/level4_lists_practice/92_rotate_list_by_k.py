numbers = [1, 2, 3, 4, 5, 6]
k = 3

if numbers:
    positions = k % len(numbers)
    rotated = numbers[-positions:] + numbers[:-positions] if positions else numbers[:]
    print("Rotated right:", rotated)
else:
    print("The list is empty")