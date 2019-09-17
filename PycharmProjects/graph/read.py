import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv", encoding='shift_jis')
# 増減を調べる --- (*1)
df['増減 (平成28年-平成12年)'] = df["平成28年"] - df["平成12年"]
# 並び替え --- (*2)
# C 列の値の大きい順 (降順) にソート df.sort_values(by='C', ascending=False)
# B 列の値の小さい順 (昇順) にソート df.sort_values(by='B')
print(df.sort_values(by=["増減 (平成28年-平成12年)"], ascending=False)[0:10])

# グラフで描画 --- (*4)
plt.bar(y=["増減"], x=["都道府県"])
# 描画実行
plt.show()






