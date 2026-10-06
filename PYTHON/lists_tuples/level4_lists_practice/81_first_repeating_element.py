numbers = [10, 5, 3, 4, 3, 5, 6]
seen = []

for number in numbers:
    if number in seen:
        print("First repeating:", number)
        break
    seen.append(number)
else:
    print("No repeating element")