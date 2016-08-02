#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 22:36:25
# @Last Modified time: 2016-04-02 22:38:57

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  nums[0], nums[1], nums[2] = nums[1], nums[2], nums[0]
  return nums


print(rotate_left3([1, 2, 3]))
