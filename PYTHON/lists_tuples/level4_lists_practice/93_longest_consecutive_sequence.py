numbers = [100, 4, 200, 1, 3, 2, 5]
number_set = set(numbers)
longest_sequence = []

for number in number_set:
    if number - 1 not in number_set:
        current_sequence = [number]
        next_number = number + 1
        while next_number in number_set:
            current_sequence.append(next_number)
            next_number += 1
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence

print("Longest consecutive sequence:", longest_sequence)