# view-source:http://www.pythonchallenge.com/pc/def/peak.html
import pickle

file = pickle.load(open("banner.p", "rb"))


# print(file)

for l in file:
  for t in l:
    print(t[0] * t[1], end=' ')

# The solution is "channel"
