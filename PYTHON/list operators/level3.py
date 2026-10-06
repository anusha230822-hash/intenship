print("===== PART 3: SLICING & INDEXING =====")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
# 41. First 5
print(nums[:5])
 
# 42. Last 5
print(nums[-5:])
 
# 43. Index 2 to 7
print(nums[2:8])
 
# 44. Every second element
print(nums[::2])
 
# 45. Every third element
print(nums[::3])
 
# 46. Reverse using slicing
print(nums[::-1])
 
# 47. Copy using slicing
copy_list = nums[:]
print(copy_list)
 
# 48. Remove first three
print(nums[3:])
 
# 49. Remove last three
print(nums[:-3])
 
# 50. Replace middle elements
temp = nums[:]
temp[4:8] = [0, 0, 0, 0]
print(temp)
 
# 51. Even-indexed elements
print(nums[0::2])
 
# 52. Odd-indexed elements
print(nums[1::2])
 
# 53. Split into two equal halves
mid = len(nums) // 2
print(nums[:mid], nums[mid:])
 
# 54. Rotate left by 2
print(nums[2:] + nums[:2])
 
# 55. Rotate right by 3
print(nums[-3:] + nums[:-3])
 