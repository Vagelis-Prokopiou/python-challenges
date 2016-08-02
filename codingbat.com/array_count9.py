def array_count9(nums):
  nines = []
  for num in nums:
    if num == 9:
      nines.append(num)

  return len(nines)

print(array_count9([1, 9, 9, 3, 9]))
