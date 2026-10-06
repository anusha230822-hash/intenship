numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

if numbers:
    current_sum = best_sum = numbers[0]
    start = best_start = best_end = 0

    for index in range(1, len(numbers)):
        if numbers[index] > current_sum + numbers[index]:
            current_sum = numbers[index]
            start = index
        else:
            current_sum += numbers[index]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = start
            best_end = index

    print("Maximum sum:", best_sum)
    print("Subarray:", numbers[best_start:best_end + 1])
else:
    print("The list is empty")