# http://www.pythonchallenge.com/pc/def/ocr.html
from urllib import request as r
import string

req = r.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

data = str(req.read()).split('</html>')[1]

data =data.replace('\\n', '').replace('<!--', '').replace('-->', '')

charList = []

for char in data:
  charList.append(char)

for x in range(len(charList)):
  if charList[x].islower():
    if charList[x-1].isupper() and charList[x+1].isupper():
      if charList[x-2].isupper() and charList[x+2].isupper():
        if charList[x-3].isupper() and charList[x+3].isupper():
          if charList[x-4].islower() and charList[x+4].islower():
            print(charList[x])

# Solution: http://www.pythonchallenge.com/pc/def/linkedlist.html
# Solution: http://www.pythonchallenge.com/pc/def/linkedlist.php
