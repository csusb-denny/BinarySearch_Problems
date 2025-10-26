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






print(kth_missing(arr, k))