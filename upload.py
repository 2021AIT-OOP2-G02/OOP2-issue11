from flask import Flask, request, render_template, jsonify
import os, glob

img_dict = {}

def list_canny():
    files = glob.glob("static/img/canny_img/*.jpg")
    # print(type(files))
    # print(files)

    for file in files:
        img_dict[os.path.basename(file)] = file
        # dict型へと格納。ファイル名とパスの二つをhtmlに渡したいため。

    print(img_dict)

    return (img_dict)


def  list_gray():
    files = glob.glob("static/img/gray_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)


def  list_binary():
    files = glob.glob("static/img/binary_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)


def  list_mozaiku():
    files = glob.glob("static/img/mozaiku_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)

def  list_upload():
    files = glob.glob("static/img/upload_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)

