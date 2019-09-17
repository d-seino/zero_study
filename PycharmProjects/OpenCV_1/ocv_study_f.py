import cv2
img = cv2.imread("hama.jpg")
# ネガポジ反転
img2 = 256 - img
cv2.imwrite("hama-nega.jpg", img2)
