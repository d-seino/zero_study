# 日本語のカレンダーを作る --- (*1)
import calendar

lc = calendar.HTMLCalendar()
body = lc.formatyear(2018, width=4)

# HTMLのヘッダとフッタを指定 --- (*2)
html = """<html><head><style>
table { padding: 8px; }
th { border-bottom: 1px solid gray; }
td { padding: 4px; vertical-align: top; }
.sun { color: red; }
.sat { color: blue; }
</style></head><body>""" + body + """
</body></html>"""

# ファイルに保存 --- (*3)
f = open("calendar2018.html", "wt")
f.write(html)