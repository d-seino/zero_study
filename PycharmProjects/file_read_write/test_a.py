# 英和辞書のデータを一行ずつ読む
word = "zoo"  # 検索単語を指定
# ファイルを開く --- (*1)
fp = open("ejdic-hand-utf8.txt", "r", encoding="utf-8")
# 一行ずつ読み取って処理する --- (*2)
for line in fp:
    if line.startswith(word):
        print(line)
fp.close()  # ファイルを閉じる --- (*3)
