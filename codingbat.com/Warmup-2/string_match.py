def string_match(a, b):
  if len(a) < len(b):
    r = len(a)-1
  else:
    r = len(b)-1
  timesFound = 0
  for x in range(r):
    if (a[x] == b[x]) and (a[x+1] == b[x+1]):
      timesFound += 1
  return timesFound

print(string_match('abc', 'axc'))
