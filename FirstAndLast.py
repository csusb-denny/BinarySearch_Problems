"""
Problem: Find First and Last position of Element in Sorted Array

Given a sorted array of integers nums and a target value target,
return the starting and ending position of target in nums.

If target is not found, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


"""

nums = [5 , 7, 7, 8, 8, 10]  
target = 8

def firstandlastPosition(nums, target):
  def findFirst(nums, target):
    l = 0
    r = len(nums) - 1
    first = -1
    while l <= r:
      middle = (l + r) // 2
      if nums[middle] == target:
        first = middle
        r = middle - 1
      if nums[middle] < target:
        l = middle + 1
      else:
        r = middle - 1
    return first
  def findLast(nums, target):
    l = 0
    r = len(nums) - 1
    last = -1 
    while l <= r:
      middle = (l+r) // 2
      if nums[middle] == target:
        last = middle
        l = middle + 1
      if nums[middle] < target:
        l = middle + 1
      else:
        r = middle - 1
    return last
  return [findFirst(nums, target), findLast(nums, target)]


print(firstandlastPosition(nums,target))