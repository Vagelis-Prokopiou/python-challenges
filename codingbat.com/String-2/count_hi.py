#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:18:36
# @Last Modified time: 2016-04-02 17:23:16

# Return the number of times that the string "hi" appears anywhere in the given string.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  times = 0
  for x in range(len(str)-1):
    if (str[x] == 'h') and (str[x+1] == 'i'):
      times += 1
  return times

print(count_hi('abc hi ho'))
