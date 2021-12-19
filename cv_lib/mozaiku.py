#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---- import ----
import cv2  # OpenCV（python版）のインポート
#rectangleメソッドは，顔を四角で囲うフィルター処理をして，画像を書き込み(rectangle_face.jpgという名前の画像で出力)
#mozaikuメソッドは，顔をモザイク処理して画像書き込み(mosaic_face.jpgという名前の画像で出力)

def rectangle():
    # 入力画像の読み込み
    img = cv2.imread('./static/img/upload_img/OneDirect.jpg')

    # カスケード型識別器の読み込み
    cascade = cv2.CascadeClassifier(r'./cv_lib/xml/haarcascade_frontalface_default.xml')

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔領域の探索
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # 顔領域を赤色の矩形で囲む
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,300), 4)

    # 結果を出力
    cv2.imwrite("./static//img/mozaiku_img/rectangle_face.jpg",img)

def mozaiku():
    import cv2

    src = cv2.imread("static/img/upload_img/OneDirect.jpg")

    def mosaic(src, ratio=0.1):
        small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    def mosaic_area(src, x, y, width, height, ratio=0.1):
        dst = src.copy()
        dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
        return dst

    #分類器を利用
    face_cascade_path = r'./cv_lib/xml/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    #前処理
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(src_gray)

    dst_face = src.copy()
    for x, y, w, h in faces:
        dst_face = mosaic_area(dst_face, x, y, w, h)
    print('検出された人数: {}'.format(len(faces)))
    cv2.imwrite("./static/img/mozaiku_img/mosaic_face.jpg", dst_face)

if __name__ == "__main__":
    rectangle()
    mozaiku()