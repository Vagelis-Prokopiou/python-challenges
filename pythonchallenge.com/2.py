# http://www.pythonchallenge.com/pc/def/ocr.html
from urllib import request as r

req = r.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')

data = str(req.read()).split('-->')[1]

data = data.replace('\\n', "")

print([x for x in data if x in 'abcdefghijklmnopqrstuvwxyz']);

# Solution: ['e', 'q', 'u', 'a', 'l', 'i', 't', 'y']

