# -*- coding: utf-8 -*-
import cv2, os

def gray(path):
    #画像読み込み
    img = cv2.imread(path)

    #読み込んだ画像をグレースケール化
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./static/img/gray_img/gray_'+os.path.basename(path), img_gray)
    # ↑引数として持ってきたfileの名前にgray_を足してファイル名としてる

    #確認用出力
    #cv2.imshow('color', img_gray)
    #cv2.waitKey(0)


    #グレースケールされた画像を二値化
    ret2, img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('./static/img/gray_img/bin_'+os.path.basename(path), img_threshold)

    #確認用出力
    #cv2.imshow('color', img_threshold)
    #cv2.waitKey(0)`
