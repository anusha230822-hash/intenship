numbers = [7, 2, 9, 4, 1, 6, 3]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print("Even:", even_numbers)
print("Odd:", odd_numbers)