numbers = [1, 2, 2, 3, 1, 4, 5]
unique_elements = [number for number in numbers if numbers.count(number) == 1]

print(unique_elements)