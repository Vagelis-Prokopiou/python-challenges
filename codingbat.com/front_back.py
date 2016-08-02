def front_back(str):
  if len(str) <= 1:
    return str
  else:
    newStr = list(str)
    h = newStr[0]
    o = newStr[-1]
    newStr[0] = o
    newStr[-1] = h
    return ''.join(newStr)



print(front_back('what are you doing'))

