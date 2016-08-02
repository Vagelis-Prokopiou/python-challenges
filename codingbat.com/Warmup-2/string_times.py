def string_times(str, n):
  if n > 0:
    return str*n
  elif n == 0:
    return ''
  else:
    return str

print(string_times('I', 1))
