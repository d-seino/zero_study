# QRコードを作成するURLの一覧 --- (*1)
urls = [
    "https://drive.google.com/open?id=1zk5mn7hVi5YN2mz81JYK74W2O4WAb92V",
    "https://drive.google.com/open?id=1tnso4EdyGtMWM5GcbR4bHe1LWfDg2Ype",
    "https://drive.google.com/open?id=1U56KIP3BivtNUhXMCp1ldtYhrq3ke4Zw",
    "https://drive.google.com/open?id=1Kd4hELrSQsj5iXbN00iyzHRGgwBLAxkj",
    "https://drive.google.com/open?id=1XmfCWwBd_1O5vkfzlMrPWac551Ga1_qs"
]

import qrcode

# 一気にQRコードを生成 --- (*2)
for url in urls:
    img = qrcode.make(url, box_size=3)
    img.show()  # 生成したQRコードを表示


