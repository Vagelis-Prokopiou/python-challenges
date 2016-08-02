#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 23:03:53

# Given an int array length 2, return True if it contains a 2 or a 3.

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
  if (2 in nums) or (3 in nums):
    return True
  return False

print(has23([2,3]))
