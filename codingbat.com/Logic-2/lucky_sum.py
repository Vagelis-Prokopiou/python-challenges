#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date: 2016-04-08 22:16:06

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  l = [a,b,c]
  if 13 in l:
    index = l.index(13)
    if index == 0:
      return 0
    else:
      return sum(l[:index])

  return sum(l)


print(lucky_sum(2, 13, 13))


# Leonidas code.
# <?php
# $lucky_sum = [13,13,3];
# $sum = 0;
# for ($i=0; $i < count($lucky_sum); $i++) {
#   if($lucky_sum[$i] == 13){break;}
#   $sum += $lucky_sum[$i];
# }
# echo $sum . '             ';
#  ?>
