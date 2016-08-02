#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date: 2016-04-08 21:53:40



# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
    if ((b == (a - 1) or b == (a + 1) or b == a) and (c <= a - 2 or c >= a + 2) and (c <= b - 2 or c >= b + 2)) \
            or ((c == (a - 1) or c == (a + 1) or c == a) and (b <= a - 2 or b >= a + 2) and (b <= c - 2 or b >= c + 2)):
        return True
    return False


print(close_far(10, 10, 8))