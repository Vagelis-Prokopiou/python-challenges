def array123(nums):
  for x in range(len(nums)-2):
    if nums[x] == 1 and (nums[x+1] == 2) and (nums[x+2] == 3):
      return True
  return False

print(array123([1, 1, 2, 4, 1,1,1,1,1,1,2,3]))
