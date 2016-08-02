#!/usr/bin/python3
# -*- coding: utf-8 -*-


# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 23:11:39

# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

def make_bricks(small, big, goal):
    if (small * 1) >= goal \
            or (big * 5) == goal \
            or ((big * 5) < goal and (big * 5) + small >= goal) \
            or ((big * 5) > goal and goal % 5 <= small):
        return True

    return False


# print(make_bricks(2, 1000000, 100003))
# print(make_bricks(3, 2, 8))
# print(make_bricks(3, 2, 8))
# print(make_bricks(1, 4, 11))
print(make_bricks(0, 3, 10))
