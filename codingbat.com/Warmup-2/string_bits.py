def string_bits(str):
  newstr = ''
  for x in range(len(str)):
    if x % 2 == 0:
      newstr += str[x]
  return newstr

print(string_bits('Heeololeo'))
