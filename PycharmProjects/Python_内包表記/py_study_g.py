# 九九のリストを作る
kuku = [(x, y, x * y) for x in range(1, 10) for y in range(1, 10)]
# 表として出力
s = ""
for x, y, z in kuku:
    s += "{0:5d}".format(z)
    if y == 9: s += "\n"
print(s)
