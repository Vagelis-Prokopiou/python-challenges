def missing_char(str, n):
  char_list = []
  for char in str:
      char_list.append(char)
  for x in range(len(char_list)):
    if x == n:
      del(char_list[x])

  return ''.join(char_list)

print(missing_char('Aloha', 4))

# Their solution.
# def missing_char(str, n):
#   front = str[:n]   # up to but not including n
#   back = str[n+1:]  # n+1 through end of string
#   return front + back
