#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date: 2016-04-07 21:58:08

# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def near_ten(num):
  if (num > 0) and (num % 10 > 7) or ((num % 10 >= 0) and (num % 10 <= 2)):
    return True
  return False

print(near_ten(48))
