# http://www.pythonchallenge.com/pc/def/channel.html

import glob
import os
import zipfile

file = zipfile.ZipFile('channel.zip', 'r')

zipfile.ZipFile.getinfo('channel.zip')
# files = glob.glob('channel/*.txt')

# for file in files:
#   fo = open(file, 'r')
#   if "nothing" in fo.read():
#     fo.close()
#     os.remove(file)
#   else:
#     print(fo.read())
#     fo.close()

