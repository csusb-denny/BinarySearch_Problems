"""
You’re given a strictly increasing sorted array of positive integers arr and an integer k.
Return the k-th missing positive number.

Examples

arr = [2,3,4,7,11], k = 5 → 9
Missing numbers are [1,5,6,8,9,10,...], the 5th is 9.

arr = [1,2,3,4], k = 2 → 6
Missing numbers are [5,6,7,...], the 2nd is 6.



#Warm Up: 
How many integers are missing up to the index i
Example:  [1,7,9]
k = 5
how do you find the missing indexes between index 0 and index 1

tempval = -1
[1, 2, 3, 4, 5, 6, 7]
for x in range arr[]
  arr[x + 1] - arr[x]
  #7 - 1 = 6 
  save that number


1  7
7 - 1 = 6
looking for 5
5 will be at index 4, also the 4th k-th missing number

target - tempval
"""
arr = [2,3,4,7,11]
k = 5

n = len(arr)

def kth_missing(arr, k):
  #if the array is empty, the k-th missing number is just k itself
  if not arr:
    return k
  #helper function:
  # how many numbers are missing?
  # if there a no missing numbers, arr[i] should have been i+1
  # so missing(i) = actual value - expected_value 
  def missing(i):
    return arr[i] -  (i + 1)

  l, r = 0, n - 1
  while l < r:
    mid = (l + r) // 2
    #if missing(mid) is already big enough (>= k)
    #the k-th missing number is at or before mid
    if missing(mid) >= k:
      r = mid
    #otherwise, its still too small -> go right
    else:
      l = mid + 1
  #at the end of loop, l == r == idx where missing(idx) >= k 
  idx = l
  #if idx == 0, the kth missing number lies entirely before
  #the first element. Since teh array starts at arr[0] >=2
  #the k-th missing number is simply 'k'
  if idx == 0:
    return k
  
  #otherwise
  #find how many numbers were missing before idx
  prev_missing = missing(idx - 1)

  #how many more numbers we need after arr[idx-1] to reach the k-th missing?
  need = k - prev_missing

  #final answer
  return arr[idx - 1] + need


print(kth_missing(arr, k))