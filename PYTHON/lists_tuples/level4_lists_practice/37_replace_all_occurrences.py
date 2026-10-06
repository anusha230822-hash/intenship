numbers = [1, 2, 3, 2, 4, 2]
old_value = 2
new_value = 99
numbers = [new_value if number == old_value else number for number in numbers]

print(numbers)