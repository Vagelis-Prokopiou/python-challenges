#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:11:42
# @Last Modified time: 2016-04-02 17:14:38


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
  if len(str) == 2:
    return str
  else:
    return str[2:] + str[:2]



print(left2('hi'))
