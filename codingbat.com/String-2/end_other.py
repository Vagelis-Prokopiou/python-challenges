#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:33:14
# @Last Modified time: 2016-04-02 17:55:41

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a == b:
    return True
  if (a[(-len(b)):] == b) or (b[(-len(a)):] == a):
    return True
  else:
    return False

print(end_other('xyz', '12xyz'))
