#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-04 22:09:11

# http://stackoverflow.com/questions/11395057/python-set-list-range-to-a-specific-value
import re
pattern = re.compile('(6)\.(.*)(7)\.')

def sum67(nums):
  if len(nums) == 0:
    return 0

  # My re solution.
  # string = ''
  # for x in range(len(nums)):
  #   string += str(nums[x]) + '.'

  # result = re.sub('(6)\.(.*?)(7)\.', '0.', string)

  # newlist = []
  # for char in result:
  #   char = char.replace('.', '0')
  #   char = char.strip()
  #   newlist.append(int(char))

  # print(newlist)
  # return(sum(newlist))

  for x in range(len(nums)):
    if nums[x] == 6:
      nums[x] = 0
      for i in range((x+1), len(nums)):
        temp = nums[i]
        nums[i] = 0
        if temp == 7:
          x += i
          break

  return sum(nums)


print(sum67([1, 2, 2, 6, 99, 99, 7, 6, 7, 6, 6, 6, 6, 7,7,7,7,7,7]))



# Leonidas code.
# nums = [1, 6, 2, 2, 7, 1, 6, 99, 99, 7]

# continuee = 0;
# sum = 0;

# for i in range(len(nums)):
#   if nums[i] == 6:
#     continuee = 6
#   if nums[i] == 7 and continuee == 6:
#     continuee = 0
#     continue
#   if continuee > 0:
#     continue
#   sum += nums[i]

# print(sum)

