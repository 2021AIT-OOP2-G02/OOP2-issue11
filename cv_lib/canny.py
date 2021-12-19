#-*- coding:utf-8 -*-
import cv2,os

def canny(path):
        
    # 入力画像を読み込み
    img = cv2.imread(path)

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 方法2(OpenCVで実装)
    dst = cv2.Canny(gray, 100, 200)

    # 結果を出力
    cv2.imwrite('./static/img/canny_img/contour_'+os.path.basename(path), dst)