#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date: 2016-04-08 21:53:40

# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
  tempA = a
  tempB = b
  tempC = c
  if a == b:
    a, b = 0, 0
  if tempA == c:
    a, c = 0, 0
  if (tempB == tempC):
    b, c = 0, 0

  return (a+b+c)

print(lone_sum(2, 3, 3))
