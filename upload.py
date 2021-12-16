from flask import Flask, request, render_template, jsonify
import os, glob

def list():
    import glob

    files = glob.glob("img/canny_img/*")
    print(files)

    upload_imgs = os.listdir("./img/gray_img")
    for f in upload_imgs:
        path = os.path.join("./img/gray_img", f)
        # if os.path.isfile(path):
        #     # ファイルの場合
        #     # print("[file  ]", f)
        # if os.path.isdir(path):
            # ファイルの場合
            # print("[folder]", f)


if __name__ == "__main__":
    post()

    
