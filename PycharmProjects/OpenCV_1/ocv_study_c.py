import cv2
img = cv2.imread("hama.jpg")
# グレイスケールに変換
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ファイルに保存
cv2.imwrite("hama-gray.jpg", gry)
