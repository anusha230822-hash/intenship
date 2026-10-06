import numpy as np
#Create an array
arr = np.array([10, 20, 30, 40, 50])
print(arr)
#print the type
print(type(arr))
#Print dtype
print(arr.dtype)
#5. Number of dimensions
print(arr.ndim)
#6. Shape of 1D array
print(arr.shape)
#7. Total number of elements
print(arr.size)
#8. Numbers from 1 to 10
arr2 = np.arange(1, 11)
print(arr2)
#9. Ten zeros
arr3 = np.zeros(10)
print(arr3)
#10. Ten ones
arr4 = np.ones(10)
print(arr4)
#11. Five 7s
arr = np.full(5, 7)
print(arr)
#12. Numbers from 0 to 20
arr = np.arange(0, 21)
print(arr)
#13. Even numbers from 2 to 20
arr = np.arange(2, 21, 2)
print(arr)
#14. Odd numbers from 1 to 19
arr = np.arange(1, 20, 2)
print(arr)
#15. Five equally spaced numbers
arr = np.linspace(0, 1, 5)
print(arr)
#16. 3×3 zeros matrix
arr = np.zeros((3, 3))
print(arr)
#17. 3×3 ones matrix
arr = np.ones((3, 3))
print(arr)
#18. 4×4 identity matrix
arr = np.eye(4)
print(arr)
#19. 2D array from nested list
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
#20. First element
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
#21. Last element
print(arr[-1])
#22. Second row
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[1])
#23. Third column
print(arr[:, 2])
#24. First three elements
print(arr[:3])
#25. Reverse array
print(arr[::-1])
#Level 2 — Array Operations & Statistics
#26. Add two arrays
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
#27. Subtract
print(a - b)
#28. Multiply
print(a * b)    
#29. Divide
print(a / b)
#30. Square
arr = np.array([1, 2, 3, 4, 5])

print(arr ** 2)
#31. Cube
print(arr ** 3)
#32. Sum
print(arr.sum())
#33. Mean
print(arr.mean())
#34. Median
print(np.median(arr))
#35. Minimum
print(arr.min())
#36. Maximum
print(arr.max())
#37. Standard deviation
print(arr.std())
#38. Variance
print(arr.var())
#39. Cumulative sum
print(np.cumsum(arr))
#40. Cumulative product
print(np.cumprod(arr))
#41. Absolute values
arr = np.array([-10, -5, 0, 5, 10])

print(np.abs(arr))
#42. Round to two decimals
arr = np.array([1.234, 2.567, 3.890])
print(np.round(arr, 2))
#43. Index of minimum value
arr = np.array([10, 50, 30, 90, 20])

print(np.argmax(arr))
#44. Index of minimum
print(np.argmin(arr))
#45. Count values greater than 50
arr = np.array([20, 60, 80, 30, 90, 40])

print(np.sum(arr > 50))
#46. Count even numbers
print(np.sum(arr % 2 == 0))
#47. Numbers divisible by 5
print(np.sum(arr % 5 == 0))
#48. Replace negative values with 0
arr = np.array([-10, 20, -5, 30, -2])

arr[arr < 0] = 0

print(arr)
#49. Replace values greater than 100 with 100
arr = np.array([10, 20, 150, 200, 50])

arr[arr > 100] = 100

print(arr)
#50. Percentage contribution
arr = np.array([10, 20, 30, 40])

percentage = (arr / arr.sum()) * 100

print(percentage)
#Level 3 — Reshaping, Indexing & Boolean Filtering
#51. Reshape 12 elements into 3×4
arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)

print(matrix)
#52. Reshape 16 elements into 4×4
arr = np.arange(1, 17)

matrix = arr.reshape(4, 4)

print(matrix)
#53. 2D to 1D using flatten()
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.flatten())
#54. 2D to 1D using ravel()
print(arr.ravel())
#55. Transpose
print(arr.T)
#56. Swap first and last rows
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

arr[[0, -1]] = arr[[-1, 0]]

print(arr)
#57. Swap first and last columns
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr[:, [0, -1]] = arr[:, [-1, 0]]

print(arr)
#58. Extract 2×2 sub-matrix
arr = np.arange(1, 17).reshape(4, 4)

print(arr[1:3, 1:3])
#59. Second row onward
print(arr[1:, :])
#60. Third column onward
print(arr[:, 2:])
#61. Values greater than 50
arr = np.array([10, 60, 30, 90, 20])
print(arr[arr > 50])
#62. Values between 20 and 80
print(arr[(arr >= 20) & (arr <= 80)])
#63. Even values
print(arr[arr % 2 == 0])
#64. Odd values
print(arr[arr % 2 != 0])
#65. Replace even values with 0
arr = np.array([1, 2, 3, 4, 5, 6])

arr[arr % 2 == 0] = 0

print(arr)
#66. Replace values below mean with mean
arr = np.array([10, 20, 30, 40, 50])
mean_value = arr.mean()
arr[arr < mean_value] = mean_value
print(arr)
#67. Sort array
arr = np.array([50, 20, 30, 10, 40])
sorted_arr = np.sort(arr)
print(sorted_arr)
#68. Sort each row
arr = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

print(np.sort(arr, axis=1))
#69. Sort each column
print(np.sort(arr, axis=0))
#70. Unique values
arr = np.array([1, 2, 2, 3, 3, 4])
print(np.unique(arr))
#