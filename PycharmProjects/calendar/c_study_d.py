# 月間カレンダーを作る --- (*1)
import calendar

lc = calendar.HTMLCalendar()
body = lc.formatmonth(2018, 1)

# ファイルに保存 --- (*2)
f = open("calendar201801.html", "wt")
f.write("<body>" + body + "</body>")
