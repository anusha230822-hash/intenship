numbers = [12, 7, 25, 3, 18]
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print("Largest:", largest)