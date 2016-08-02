def array_front9(nums):
  a = False
  if len(nums) > 4:
    for x in range(4):
      if nums[x] == 9:
        a = True
        break
      else:
        a = False
  elif len(nums) <= 3 and (len(nums) > 0):
    for x in range(len(nums)):
      if nums[x] == 9:
        a = True
        break
      else:
        a = False
  else:
    if len(nums) == 0:
      a = False

  return a



print(array_front9([1, 2, 9, 3, 4]))


# Their code
# def array_front9(nums):
#   # First figure the end for the loop
#   end = len(nums)
#   if end > 4:
#     end = 4

#   for i in range(end):  # loop over index [0, 1, 2, 3]
#     if nums[i] == 9:
#       return True
#   return False
