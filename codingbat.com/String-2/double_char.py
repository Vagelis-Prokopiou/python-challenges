#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:15:43
# @Last Modified time: 2016-04-02 17:17:44

# Given a string, return a string where for every char in the original, there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  newstr = ''
  for char in str:
    newstr += char * 2
  return newstr

print(double_char('Hi-There'))
