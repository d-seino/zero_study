import qrcode  # qrcodeを起動

img = qrcode.make('hoge')  # ''内の文字をQRコードに変換
img.show()  # 生成したQRコードを表示
img.save('qr_img.png')  # QRコードに名前をつけて保存
