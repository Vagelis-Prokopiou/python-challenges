#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 22:16:07
# @Last Modified time: 2016-04-02 22:35:13

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

# make_pi() → [3, 1, 4]


def make_pi():
  l = list({3,1,4})
  rl = []
  for x in range(len(l)):
    if l[x] == 3:
      rl.insert(0, l[x])
    elif l[x] == 1:
      rl.insert(1, l[x])
    else:
      if l[x] == 4:
        rl.insert(2, l[x])

  return rl


print(make_pi())
