# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(text):
  if len(text) > 0:
    newstr = ''
    for x in range(1, len(text)+1):
      newstr = str(newstr) + str(text[:x])

  return newstr


print(string_splosion('ab'))
