from flask import Flask, request, render_template, jsonify
import os, glob

img_dict = {}

def list_canny():
    img_dict = {}
    files = glob.glob("static/img/canny_img/*.jpg")
    # print(type(files))
    # print(files)

    for file in files:
        img_dict[os.path.basename(file)] = file
        # dict型へと格納。ファイル名とパスの二つをhtmlに渡したいため。

    print(img_dict)

    return (img_dict)


def  list_gray():
    img_dict = {}
    files = glob.glob("static/img/gray_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)


def  list_binary():
    img_dict = {}
    files = glob.glob("static/img/binary_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)


def  list_mozaiku():
    img_dict = {}
    files = glob.glob("static/img/mozaiku_img/*.jpg")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)

def  list_upload():
    img_dict = {}
    files = glob.glob("static/img/upload_img/*.png")

    for file in files:
        img_dict[os.path.basename(file)] = file

    return (img_dict)

