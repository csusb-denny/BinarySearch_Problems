nums = [1,3,5,6]
target = 5

def SearchInsertPosition(nums, target):
  l = 0
  r = len(nums) - 1
  while(l <= r):
    mid = (l + r) // 2
    if nums[mid] == target:
      return mid
    if nums[mid] > target:
      r = mid - 1
    else:
      l = mid + 1
  return l

print(SearchInsertPosition(nums, target))