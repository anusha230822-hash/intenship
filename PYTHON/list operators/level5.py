print("===== PART 5: INTERMEDIATE PROBLEM SOLVING =====")
 
# 71. Remove duplicates without set()
names = ["Anusha", "King", "Anusha", "Teju", "King", "Yashu"]
result = []
for n in names:
    if n not in result:
        result.append(n)
print(result)
 
# 72. Find all duplicate elements
seen = []
dups = []
for n in names:
    if n in seen and n not in dups:
        dups.append(n)
    else:
        seen.append(n)
print("Duplicates:", dups)
 
# 73. All unique elements (elements that appear only once)
uniq = []
for n in names:
    if names.count(n) == 1:
        uniq.append(n)
print("Unique:", uniq)
 
# 74. Common elements between two lists
l1 = ["Anusha", "King", "Yashu"]
l2 = ["Yashu", "Teju", "Anusha"]
common = []
for x in l1:
    if x in l2:
        common.append(x)
print(common)
 
# 75. In first list but not in second
diff = []
for x in l1:
    if x not in l2:
        diff.append(x)
print(diff)
 
# 76. Merge two lists and remove duplicates
merged = l1 + l2
final = []
for x in merged:
    if x not in final:
        final.append(x)
print(final)
 
# 77. Intersection of three lists
a = ["Anusha", "King", "Yashu", "Teju"]
b = ["Anusha", "Yashu", "Teju"]
c = ["Yashu", "Teju", "King"]
result = []
for x in a:
    if x in b and x in c:
        result.append(x)
print(result)
 
# 78. Union of two lists without set()
union = []
for x in l1:
    if x not in union:
        union.append(x)
for x in l2:
    if x not in union:
        union.append(x)
print(union)
 
# 79. Missing number from 1 to N
nums = [1, 2, 3, 5, 6]
n = 6
expected = n * (n + 1) // 2
actual = 0
for x in nums:
    actual += x
print("Missing number =", expected - actual)
 
# 80. First non-repeating element
names = ["Anusha", "King", "Anusha", "Teju", "King"]
for x in names:
    if names.count(x) == 1:
        print("First non-repeating:", x)
        break
 
# 81. First repeating element
seen = []
for x in names:
    if x in seen:
        print("First repeating:", x)
        break
    seen.append(x)
 
# 82. Most frequent element
names = ["Anusha", "King", "Anusha", "Teju", "Anusha", "King"]
best = names[0]
for x in names:
    if names.count(x) > names.count(best):
        best = x
print("Most frequent:", best)
 
# 83. Least frequent element
least = names[0]
for x in names:
    if names.count(x) < names.count(least):
        least = x
print("Least frequent:", least)
 
# 84. All pairs whose sum equals a number
nums = [1, 2, 3, 4, 5, 6]
target = 7
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
 
# 85. All triplets whose sum equals a number
nums = [1, 2, 3, 4, 5, 6]
target = 12
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                print(nums[i], nums[j], nums[k])
 