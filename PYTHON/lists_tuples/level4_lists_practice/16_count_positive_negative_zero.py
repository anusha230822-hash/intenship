numbers = [8, -3, 0, 12, -7, 0, 4]
positive = negative = zero = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)