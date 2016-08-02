#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 22:59:25

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
  l = []
  l.append(a[1])
  l.append(b[1])
  return l

print(middle_way([5, 2, 9], [1, 4, 5]))
