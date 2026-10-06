print("===== PART 2: LIST METHODS =====")
 
# 21. append()
names = ["Anusha", "King"]
names.append("Yashu")
print(names)
 
# 22. extend()
names.extend(["Teju", "Anusha"])
print(names)
 
# 23. Insert at 3rd position (index 2)
names = ["Anusha", "King", "Teju"]
names.insert(2, "Yashu")
print(names)
 
# 24. remove()
names.remove("King")
print(names)
 
# 25. pop() last
names = ["Anusha", "King", "Yashu", "Teju"]
names.pop()
print(names)
 
# 26. pop(index)
names.pop(1)
print(names)
 
# 27. del
names = ["Anusha", "King", "Yashu", "Teju"]
del names[2]
print(names)
 
# 28. clear()
names.clear()
print(names)
 
# 29. index()
names = ["Anusha", "King", "Yashu", "Teju"]
print("Index of Yashu =", names.index("Yashu"))
 
# 30. count()
names = ["Anusha", "King", "Anusha", "Teju", "Anusha"]
print("Anusha count =", names.count("Anusha"))
 
# 31. Sort ascending
marks = [55, 90, 72, 38, 85]
marks.sort()
print(marks)
 
# 32. Sort descending
marks.sort(reverse=True)
print(marks)
 
# 33. reverse()
marks.reverse()
print(marks)
 
# 34. Sorted copy (original same)
marks = [55, 90, 72, 38, 85]
new_marks = sorted(marks)
print("Original:", marks)
print("Sorted copy:", new_marks)
 
# 35. Add five user-entered values
my_list = []
for i in range(5):
    value = input("Enter value: ")
    my_list.append(value)
print(my_list)
 
# 36. Remove all occurrences of a number
nums = [1, 2, 3, 2, 4, 2, 5]
while 2 in nums:
    nums.remove(2)
print(nums)
 
# 37. Replace all occurrences of one value with another
nums = [1, 2, 3, 2, 4, 2]
for i in range(len(nums)):
    if nums[i] == 2:
        nums[i] = 99
print(nums)
 
# 38. Insert an element after every occurrence of a value
names = ["Anusha", "King", "Anusha", "Teju"]
result = []
for n in names:
    result.append(n)
    if n == "Anusha":
        result.append("Yashu")
print(result)
 
# 39. Frequency of every element
names = ["Anusha", "King", "Anusha", "Teju", "King", "Anusha"]
freq = {}
for n in names:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print(freq)
 
# 40. Compare two lists (same elements, any order)
l1 = ["Anusha", "King", "Yashu"]
l2 = ["Yashu", "Anusha", "King"]
if sorted(l1) == sorted(l2):
    print("Same elements")
else:
    print("Different elements")
 