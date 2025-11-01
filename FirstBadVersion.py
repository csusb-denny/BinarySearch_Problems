"""
You are a quality control engineer.
You are given:
n versions of a product [1, 2, 3, ..., n]
one of these versions is the first bad version

!All version after the first bad one are also bad

You have an API isBadVersion(version) that returns:
true if the version is bad
false if the version is good

Task:
Find the first bad version using the min number of calls to the API

Example:
n = 5; bad = 4
isBadVersion(3) -> false
isBadVersion(4) -> true
...(5) -> True

output: 4
"""
arr = [1,4,4,4,5,6,7,8,9,10]
bad = 4

def isBadVersion(arr, bad):
  l = 0
  r = len(arr) - 1
  badIndex = -1

  while l <= r:
    mid = (l+r) // 2
    if arr[mid] == bad:
      badIndex = mid
      r = mid - 1 #look left for earlier bad
    elif bad < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1 #shift right
  return badIndex

print(isBadVersion(arr, bad))

#search insert position
"""
given sorted array of DISTINCT integers and a target value
return the INDEX if the target is found
if not, return the index where it WOULD be inserted in order
Example:
nums = [1,3,5,6], target = 5
output = 2

nums = [1,3,5,6], target = 7
output = 4
"""

nums = [1,3,5,6]
target = 9

def insertDistinct(nums, target):
  left = 0
  right = len(nums) - 1
  while (left <= right):
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    elif target < nums[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return left

print(insertDistinct(nums,target))

#find peak element
"""
A peak element is an element that is strictly greater than its neighbors
Given a 0-indexed array nums, find a peak index

Example:
nums = [1,2,3,1]
Output:2
3 is a peak at index 2

nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explaination 2 and 6 are both peaks

"""
nums2 = [1,2,1,3,5,6,4]
def PeakElement(nums2):
  answer = []
  for x in range(1, len(nums2) - 1):
    current = nums2[x]
    left = nums2[x-1]
    right = nums2[x+1]
    if current > left and current > right:
      answer.append(x)
  return answer
print(PeakElement(nums2))