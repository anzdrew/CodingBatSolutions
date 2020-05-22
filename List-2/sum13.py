# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  
  i, sum = 0, 0
  
  while i < len(nums):
    if nums[i] == 13:
      i += 1
    else:
      sum += nums[i]
    i += 1
    
  return sum
