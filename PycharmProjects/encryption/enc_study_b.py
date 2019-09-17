c = "EW@@"
b = "1234"
# 復号化
a = []
for bb, cc in zip(b, c):
  aa = chr(ord(bb) ^ ord(cc))
  a += [aa]
print("".join(a))
