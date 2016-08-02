## http://www.pythonchallenge.com/pc/def/linkedlist.php
#from urllib import request as r

## req = r.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
#var = 12345
#var = 16044/2
#var = 82682
#var = 63579
#var = 52899

#while True:
#  for x in range(400):
#    try:
#      req = r.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(var))
#      var = str(req.read()).split('is ')[1].split('\'')[0]
#      if int(var) == 16044:
#        var = 16044/2
#      else:
#        print(var)
#    except Exception as e:
#      print(e)
#      print('<' + '--'*5 + ' Ending the program ' + '--'*5 + '>')
#      exit()

# Solution: peak.html












#def sleep_in(weekday, vacation):
#  if weekday == vacation:
#    return False
#  elif weekday != vacation:
#    if vacation == True:
#      return True
#  else:
#     return False

#def sleep_in(weekday, vacation):
#  if not weekday or vacation:
#    return True
#  else:
#    return False


#print(sleep_in(True, True))

def missing_char(str, n):
  char_list = []
  for char in str:
      char_list.append(char)
  for x in range(len(char_list)):
    if x == n:
      del(char_list[x])

  return ''.join(char_list)




print(missing_char('Aloha', 4))

















