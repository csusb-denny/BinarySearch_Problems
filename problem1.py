"""
Example 1: Find the smallest Element Greater than Target (Ceiling)
You are given a sorted array of integers and a target value

Task: Return the smallest element in the array that is strictly greater than the target
"""
arr = [2, 4, 6, 8, 10]
target = 5 #expected output: 6

#Given the prompt we want to return x > target in which x is the least of its sublist

def binary_search(arr, target):
  left = 0                        #left pointer
  right = len(arr) - 1            #right pointer
  result = -1                     #store best candidate found
  while left <= right:
    middle = (left + right) // 2  #We use // instead of / because we want the integer value not rounded up 

    if arr[middle] > target:
      result = arr[middle]        #store this as a candidate
      right = middle - 1          #look left for a smaller candidate
    else:                         
      left = middle + 1           #go right if the arr[middle] <= target

  return result
print(binary_search(arr, target))