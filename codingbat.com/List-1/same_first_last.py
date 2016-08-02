#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 22:16:07
# @Last Modified time: 2016-04-02 22:19:09

# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True


def same_first_last(nums):
  if (len(nums) >= 1) and (nums[0] == nums[-1]):
    return True
  return False

print(same_first_last([0, 6, 1, 2, 6]))
