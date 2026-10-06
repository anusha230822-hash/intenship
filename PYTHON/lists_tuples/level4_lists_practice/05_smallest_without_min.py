numbers = [12, 7, 25, 3, 18]
smallest = numbers[0]

for number in numbers[1:]:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)