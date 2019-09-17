import re  # 正規表現を使う --- (*1)

# 辞書ファイルを開く --- (*2)
fdic = open("ejdic-hand-utf8.txt", "rt", encoding="utf-8")
# 書き込み先ファイルを開く
fw = open("q-list.txt", "wt")

# 一行ずつ読んで、qから始まる4文字の単語を調べる --- (*3)
for line in fdic:
    if re.match(r"q[a-z]{3}\s", line):
        fw.write(line)
        print(line.strip())

# ファイルを閉じる --- (*4)
fw.close()
fdic.close()