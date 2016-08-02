#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Date:   2016-04-02 15:42:22
# @Last Modified by:   Vagelis Prokopiou

# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
  if len(str) < 3:
    return str * 3
  else:
    return str[-2:] * 3


print(extra_end('Hello'))

