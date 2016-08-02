#!/usr/bin/python3
# -*- coding: utf-8 -*-


# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 23:11:39

# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
#
# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
    if (big * 5) <= goal:
        if (goal - (big * 5) <= small) and (goal - (big * 5) >= 0):
            return goal - (big * 5)
    elif (big * 5) > goal:
        if small == goal:
            return small
        for x in range(1, big):
            if (x * 5) + small >= goal:
                return goal - (x * 5)
            return -1

    return -1


print(make_chocolate(1, 2, 7))
