"""
Example 2: Find the floor of a Target
You're given a sorted array of int and target value
Return the largest element in the array that is strictly less than the target

If no element exist return -1
"""
arr = [2, 4, 6, 8, 10]
target = 7
#expected output: 6 (6 is the largest element < 7)

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  result = -1
  while left <= right:
    middle = (left + right) // 2
    if arr[middle] == target:
      right = middle - 1
    if target > arr[middle]:
      left = middle + 1
      result = arr[middle]
    else:
      right = middle - 1
  return result

print(binary_search(arr, target))