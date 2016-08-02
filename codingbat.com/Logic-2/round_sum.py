#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date: 2016-04-08 21:53:40


# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3


def round10(num):
    if num % 10 == 0:
        return num
    elif (num % 10) >= 5:
        return num + (10-(num % 10))
    elif (num % 10) < 5:
        return num - (num % 10)


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


print(round_sum(16, 17, 18))
# print(round10(34))
