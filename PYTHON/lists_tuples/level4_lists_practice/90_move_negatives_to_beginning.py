numbers = [3, -1, 4, -7, 0, -2, 8]
negative_numbers = [number for number in numbers if number < 0]
other_numbers = [number for number in numbers if number >= 0]

print(negative_numbers + other_numbers)