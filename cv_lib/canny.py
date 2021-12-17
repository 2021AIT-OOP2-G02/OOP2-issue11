#-*- coding:utf-8 -*-
import cv2

# 入力画像を読み込み
img = cv2.imread('../img/upload_img/test.png')

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 方法2(OpenCVで実装)
dst = cv2.Canny(gray, 100, 200)

# 結果を出力
cv2.imwrite('../img/canny_img/test.png', dst)