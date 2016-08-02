def front_times(str, n):
  if n > 0:
    if len(str) > 3:
      return str[:3] * n
    else:
      return str * n
  elif n == 0:
    return ''


print(front_times('Itah', 0))
