from collections import Counter

first = [1, 2, 2, 3]
second = [3, 2, 1, 2]

print("Same elements with same counts:", Counter(first) == Counter(second))