# ライブラリを取り込む --- (*1)
import openpyxl as excel

# 新規ワークブックを作る --- (*2)
wb = excel.Workbook()
# アクティブなワークシートを得る --- (*3)
ws = wb.active
# A1のセルに値を設定 --- (*4)
ws["A1"] = "こんにちは"
# ファイルを保存 --- (*5)
wb.save("hello.xlsx")
