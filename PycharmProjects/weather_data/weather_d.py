import pandas as pd
import re

# CSVデータを読み込む
df = pd.read_csv("cities-data.csv", encoding="SHIFT_JIS")
# データを集計
sumd = {}  # 辞書型を初期化
for row in df.iterrows():
    ymd = row[1]["年月日"]
    md = re.sub('^\d+/', '', ymd)
    if not (md in sumd): sumd[md] = [0, 0, 0, 0]
    # 各都市の降水量を加算する --- (*1)
    for i in range(1, 5):
        sumd[md][i - 1] += row[1][i]

# 表として出力するための処理 --- (*2)
df = pd.DataFrame.from_dict(sumd).T
df.columns = ("横浜", "箱根", "木更津", "御殿場")

# 並び替えて先頭の10件を表示 --- (*3)
print(df.sort_values(by="木更津", ascending=True)[0:10])