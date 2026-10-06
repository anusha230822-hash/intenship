print("===== PART 1: BASIC LIST OPERATIONS =====")
 
# 1. List of 10 integers
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in nums:
    print(x)
 
# 2. List of 5 names, first and last
names = ["Anusha", "King", "Yashu", "Teju", "Anusha"]
print("First:", names[0], "| Last:", names[-1])
 
# 3. Length without len()
names = ["Anusha", "King", "Yashu", "Teju"]
count = 0
for n in names:
    count += 1
print("Length =", count)
 
# 4. Largest without max()
nums = [12, 45, 7, 89, 23]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest =", largest)
 
# 5. Smallest without min()
smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n
print("Smallest =", smallest)
 
# 6. Sum without sum()
total = 0
for n in nums:
    total += n
print("Sum =", total)
 
# 7. Count how many times a number occurs
nums = [1, 2, 3, 2, 4, 2, 5]
target = 2
c = 0
for n in nums:
    if n == target:
        c += 1
print(target, "occurs", c, "times")
 
# 8. Check element exists
names = ["Anusha", "King", "Yashu", "Teju"]
if "Yashu" in names:
    print("Yashu is present")
else:
    print("Yashu is not present")
 
# 9. Print using for loop
for n in names:
    print(n)
 
# 10. Print in reverse order
for i in range(len(names) - 1, -1, -1):
    print(names[i])
 
# 11. Only even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    if n % 2 == 0:
        print(n)
 
# 12. Only odd numbers
for n in nums:
    if n % 2 != 0:
        print(n)
 
# 13. Squares
squares = []
for n in nums:
    squares.append(n * n)
print(squares)
 
# 14. Cubes
cubes = []
for n in nums:
    cubes.append(n ** 3)
print(cubes)
 
# 15. Average
total = 0
for n in nums:
    total += n
print("Average =", total / len(nums))
 
# 16. Count positive, negative, zero
nums = [5, -3, 0, 8, -1, 0, 7]
pos = neg = zero = 0
for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos, "Negative:", neg, "Zero:", zero)
 
# 17. Second largest
nums = [10, 40, 30, 20, 40]
unique = sorted(set(nums))
print("Second largest =", unique[-2])
 
# 18. Second smallest
print("Second smallest =", unique[1])
 
# 19. Swap first and last
marks = [90, 80, 70, 60]
marks[0], marks[-1] = marks[-1], marks[0]
print(marks)
 
# 20. Copy list without copy()
a = ["Anusha", "King", "Yashu"]
b = []
for x in a:
    b.append(x)
print(b)
 