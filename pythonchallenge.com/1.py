import string

# 1st challenge.
# print(2**38) = 274877906944

# 2nd challenge.
# See: http://stackoverflow.com/questions/10329290/python-3-x-using-string-maketrans-in-order-to-create-a-unicode-character-tran
old = 'abcdefghijklmnopqrstuvwxyz'
new = 'cdefghijklmnopqrstuvwxyzab'
trans_table = str.maketrans(old, new)
msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
print(msg.translate(trans_table))
# Solution: i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url
# Make the "map" -> "ocr".
