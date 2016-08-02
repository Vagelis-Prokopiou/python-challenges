#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 22:45:25

# Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array.

# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
  nl = []
  if nums[0] > nums[-1]:
    target = nums[0]
  else:
    target = nums[-1]

  for x in range(len(nums)):
    nl.append(target)

  return nl

print(max_end3([4, 2, 3, 4, 5]))
