numbers = [10, 9, 2, 5, 3, 7, 101, 18]

if numbers:
    lengths = [1] * len(numbers)
    previous = [-1] * len(numbers)

    for current_index in range(len(numbers)):
        for earlier_index in range(current_index):
            if numbers[earlier_index] < numbers[current_index]:
                if lengths[earlier_index] + 1 > lengths[current_index]:
                    lengths[current_index] = lengths[earlier_index] + 1
                    previous[current_index] = earlier_index

    index = max(range(len(numbers)), key=lambda position: lengths[position])
    sequence = []
    while index != -1:
        sequence.append(numbers[index])
        index = previous[index]
    sequence.reverse()
    print("Longest increasing subsequence:", sequence)
else:
    print("The list is empty")