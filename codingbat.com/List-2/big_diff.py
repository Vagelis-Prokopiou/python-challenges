#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-03 09:03:08

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
  nums = sorted(nums)
  nums.remove(nums[0])
  nums.remove(nums[-1])
  total = 0
  for n in nums:
    total += n
  return (total//len(nums))


print(centered_average([1, 2, 3, 4, 100]))
