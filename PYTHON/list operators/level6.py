print("===== PART 6: ADVANCED LIST PROBLEMS =====")
 
# 86. Maximum sum of any two elements
nums = [5, 9, 2, 7, 1]
s = sorted(nums)
print("Max sum =", s[-1] + s[-2])
 
# 87. Minimum sum of any two elements
print("Min sum =", s[0] + s[1])
 
# 88. Maximum difference between two elements
print("Max difference =", s[-1] - s[0])
 
# 89. Move all zeros to the end (order same)
nums = [0, 1, 0, 3, 12, 0, 5]
non_zero = []
zeros = []
for x in nums:
    if x == 0:
        zeros.append(x)
    else:
        non_zero.append(x)
print(non_zero + zeros)
 
# 90. Negative numbers to the beginning
nums = [4, -1, 3, -5, 2, -8]
neg = []
others = []
for x in nums:
    if x < 0:
        neg.append(x)
    else:
        others.append(x)
print(neg + others)
 
# 91. Separate even and odd (original order)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
odds = []
for x in nums:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
print("Evens:", evens)
print("Odds:", odds)
print("Combined:", evens + odds)
 
# 92. Rotate a list by K positions (to the right)
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(nums)
print(nums[-k:] + nums[:-k])
 
# 93. Longest consecutive sequence of integers
nums = [100, 4, 200, 1, 3, 2]
nums = sorted(set(nums))
longest = 1
current = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        current += 1
    else:
        current = 1
    if current > longest:
        longest = current
print("Longest consecutive length =", longest)
 
# 94. Longest increasing subsequence
nums = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(nums)
length = [1] * n          # length[i] = LIS ending at i
prev = [-1] * n           # to remember the path
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and length[j] + 1 > length[i]:
            length[i] = length[j] + 1
            prev[i] = j
end = 0
for i in range(n):
    if length[i] > length[end]:
        end = i
lis = []
while end != -1:
    lis.append(nums[end])
    end = prev[end]
lis.reverse()
print("LIS =", lis, "Length =", len(lis))
 
# 95. Maximum sum subarray (Kadane's idea)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best = nums[0]
current = nums[0]
for i in range(1, len(nums)):
    current = max(nums[i], current + nums[i])
    best = max(best, current)
print("Maximum subarray sum =", best)
 
# 96. All subarrays whose sum equals a given number
nums = [1, 2, 3, 4, 5]
target = 9
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total == target:
            print(nums[i:j + 1])
 
# 97. The subarray with the largest sum (print the subarray)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best_sum = nums[0]
best_start = best_end = 0
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total > best_sum:
            best_sum = total
            best_start = i
            best_end = j
print("Subarray:", nums[best_start:best_end + 1], "Sum =", best_sum)
 
# 98. Product of all elements except current (no division)
nums = [1, 2, 3, 4]
result = []
for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if i != j:
            product *= nums[j]
    result.append(product)
print(result)
 
# 99. Flatten a nested list
def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))   # list inside list -> call again
        else:
            flat.append(item)
    return flat
 
print(flatten([1, [2, 3], [4, [5, 6]]]))
 
# 100. MINI PROJECT: Student records
# Each record = [name, marks, course]
records = [
    ["Anusha", 92, "Python"],
    ["King", 78, "Java"],
    ["Yashu", 85, "Python"],
    ["Teju", 45, "Java"],
    ["Anusha", 92, "Python"],     # duplicate record
    ["Teju", 88, "AI"],
    ["King", 35, "AI"],
]
 
# (f) Duplicate student records
seen = []
duplicates = []
for r in records:
    if r in seen and r not in duplicates:
        duplicates.append(r)
    else:
        seen.append(r)
print("Duplicate records:", duplicates)
 
# Remove duplicates so that results are correct
students = []
for r in records:
    if r not in students:
        students.append(r)
 
# (a) Topper
topper = students[0]
for s in students:
    if s[1] > topper[1]:
        topper = s
print("Topper:", topper[0], topper[1])
 
# (b) Class average
total = 0
for s in students:
    total += s[1]
print("Class average =", total / len(students))
 
# (c) Students who scored above 80
print("Above 80:")
for s in students:
    if s[1] > 80:
        print("  ", s[0], s[1])
 
# (d) Lowest scorer
lowest = students[0]
for s in students:
    if s[1] < lowest[1]:
        lowest = s
print("Lowest scorer:", lowest[0], lowest[1])
 
# (e) Rank students by marks (highest first)
ranked = sorted(students, key=lambda s: s[1], reverse=True)
print("Ranking:")
rank = 1
for s in ranked:
    print("  Rank", rank, "-", s[0], s[1])
    rank += 1
 
# (g) Group students by course
groups = {}
for s in students:
    course = s[2]
    if course not in groups:
        groups[course] = []
    groups[course].append(s)
print("Groups by course:")
for course in groups:
    print("  ", course, "->", [x[0] for x in groups[course]])
 
# (h) Highest scorer in each course
print("Highest scorer in each course:")
for course in groups:
    top = groups[course][0]
    for s in groups[course]:
        if s[1] > top[1]:
            top = s
    print("  ", course, "->", top[0], top[1])
 
# (i) Final result: Distinction (>=75) / Pass (>=40) / Fail (<40)
print("Final Result:")
final_result = []
for s in students:
    if s[1] >= 75:
        status = "Distinction"
    elif s[1] >= 40:
        status = "Pass"
    else:
        status = "Fail"
    final_result.append([s[0], s[1], s[2], status])
for r in final_result:
    print("  ", r)
 

