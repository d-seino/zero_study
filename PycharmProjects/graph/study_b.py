import pandas as pd
import matplotlib

matplotlib.style.use('ggplot')

df = pd.read_csv("population.csv", encoding="SHIFT_JIS")
# 増減を調べ増加順に並び替える
df['増減'] = df["平成28年"] - df["平成27年"]
df = df.sort_values(by=["増減"], ascending=False)
# 上位5位を抽出
top = df[0:5]
# 円グラフで描画 --- (*1)
top["増減"].plot.pie(labels=top["都道府県"], autopct='%.0f')
