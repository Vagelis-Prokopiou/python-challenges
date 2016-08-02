#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:29:24
# @Last Modified time: 2016-04-02 17:33:01

# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
  times = 0
  for x in range(len(str)-3):
    if (str[x] == 'c') and (str[x+1] == 'o') and (str[x+3] == 'e'):
      times += 1
  return times


print(count_code('cozexxcope'))
