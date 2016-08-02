#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 16:57:02
# @Last Modified time: 2016-04-02 17:09:53

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
  if (len(a) > 1) and (len(b) > 1):
    return a[1:] + b[1:]
  elif (len(a) <= 1) and (len(b) <= 1):
    return ''
  elif (len(a) <= 1) and (len(b) > 1):
    return b[1:]
  else:
    if (len(a) > 1) and (len(b) <= 1):
      return a[1:]

print(non_start('There', 'Ar'))
