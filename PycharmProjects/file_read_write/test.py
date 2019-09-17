# ファイルにShift_JISで格言を書き込む
fw = open("kakugen-sjis.txt", "wt", encoding="shift_jis")
fw.write("光陰矢のごとし")
fw.close()

# ファイルから格言を読み込む
fr = open("kakugen-sjis.txt", "rt", encoding="shift_jis")
text = fr.read()
print(text)
fr.close()