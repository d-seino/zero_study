import openpyxl as excel

# 新規ワークブックを作る
wb = excel.Workbook()
ws = wb.active

# 九九の表を作る
for i in range(1, 10):
    for j in range(1, 10):
        v = i * j
        ws.cell(column=j, row=i, value=v) # --- (*1)

wb.save("kuku.xlsx")
