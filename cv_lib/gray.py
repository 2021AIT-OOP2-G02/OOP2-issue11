# -*- coding: utf-8 -*-
import cv2


#画像読み込み
img = cv2.imread('img/upload_img/test.png')

#読み込んだ画像をグレースケール化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('img/gray_img/gray.jpg', img_gray)

#確認用出力
#cv2.imshow('color', img_gray)
#cv2.waitKey(0)


#グレースケールされた画像を二値化
ret2, img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
cv2.imwrite('img/threshold_img/threshold.jpg', img_threshold)

#確認用出力
#cv2.imshow('color', img_threshold)
#cv2.waitKey(0)
