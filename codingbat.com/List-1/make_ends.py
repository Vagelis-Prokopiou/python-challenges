#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 23:03:53

# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
  if len(nums) == 1:
    return nums*2
  else:
    l = []
    l.append(nums[0])
    l.append(nums[-1])
    return l

print(make_ends([1,10,56,78,23]))
