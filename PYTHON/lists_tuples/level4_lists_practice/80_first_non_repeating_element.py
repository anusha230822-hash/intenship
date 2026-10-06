numbers = [4, 5, 1, 2, 1, 4, 5]

for number in numbers:
    if numbers.count(number) == 1:
        print("First non-repeating:", number)
        break
else:
    print("No non-repeating element")