print("===== PART 4: LIST COMPREHENSION =====")
 
# 56. 1 to 50
print([i for i in range(1, 51)])
 
# 57. Squares 1 to 20
print([i ** 2 for i in range(1, 21)])
 
# 58. Cubes 1 to 20
print([i ** 3 for i in range(1, 21)])
 
# 59. Even numbers 1 to 100
print([i for i in range(1, 101) if i % 2 == 0])
 
# 60. Odd numbers 1 to 100
print([i for i in range(1, 101) if i % 2 != 0])
 
# 61. Divisible by both 3 and 5
print([i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0])
 
# 62. Uppercase
names = ["Anusha", "King", "Yashu", "Teju"]
print([n.upper() for n in names])
 
# 63. Lowercase
print([n.lower() for n in names])
 
# 64. Words with more than 5 characters
words = ["Anusha", "King", "Yashu", "Teju", "Students"]
print([w for w in words if len(w) > 5])
 
# 65. Numbers greater than 50
nums = [10, 55, 80, 30, 99, 45]
print([n for n in nums if n > 50])
 
# 66. Replace negatives with 0
nums = [5, -2, 8, -7, 0, 3]
print([n if n >= 0 else 0 for n in nums])
 
# 67. "Even" or "Odd" for each number
nums = [1, 2, 3, 4, 5]
print(["Even" if n % 2 == 0 else "Odd" for n in nums])
 
# 68. Length of every word
print([len(n) for n in names])
 
# 69. Vowels from a string
text = "Anusha King Yashu Teju"
print([ch for ch in text if ch.lower() in "aeiou"])
 
# 70. Numbers whose square is greater than 100
print([n for n in range(1, 21) if n * n > 100])