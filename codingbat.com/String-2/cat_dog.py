#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:23:37
# @Last Modified time: 2016-04-02 17:29:08

# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  cats = 0
  dogs = 0
  for x in range(len(str)-2):
    if (str[x] == 'c') and (str[x+1] == 'a') and (str[x+2] == 't'):
      cats += 1
    if (str[x] == 'd') and (str[x+1] == 'o') and (str[x+2] == 'g'):
      dogs += 1
  if cats == dogs:
    return True
  else:
    return False


print(cat_dog('1cat1cadodog'))
