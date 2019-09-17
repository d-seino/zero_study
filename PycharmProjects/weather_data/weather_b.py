import pandas as pd
import re

# CSVデータを読み込む
df = pd.read_csv("data-kai.csv", encoding="SHIFT_JIS")
# 10年分のデータを集計
sumd = {}  # 辞書型を初期化
for row in df.iterrows():
    ymd = row[1]["年月日"]
    tenki = row[1]["天気概況"]
    md = re.sub(r'\d{4}\/', '', ymd)  # 月/日だけにする
    if not (md in sumd): sumd[md] = 0
    if tenki.find("雨") >= 0: sumd[md] += 1

# 集計結果を並び替え
result = sorted(sumd.items(), key=lambda n: n[1])
# 上位25件を表示
top = result[0:25]
print(pd.DataFrame(top, columns=['日付', '雨の日数']))
