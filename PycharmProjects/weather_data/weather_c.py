import pandas as pd
import re

# CSVデータを読み込む
df = pd.read_csv("data-kai.csv", encoding="SHIFT_JIS")
# 10年分のデータを集計
sumd = {}  # 辞書型を初期化
for row in df.iterrows():
    ymd = row[1]["年月日"]
    kousui = row[1]["降水量の合計"]
    mo = re.match('\d+/(\d+)/(\d+)', ymd)
    m = int(mo.group(1))  # 月
    d = int(mo.group(2))  # 日
    # 9月から11月のデータだけを利用する
    if not (9 <= m <= 11): continue
    md = str(m) + "/" + str(d)
    if not (md in sumd): sumd[md] = 0
    sumd[md] += kousui
# 集計結果を並び替え
result = sorted(sumd.items(), key=lambda n: n[1])
# 上位20件を表示
top20 = result[0:20]
print(pd.DataFrame(top20, columns=['日付', '降水量']))

