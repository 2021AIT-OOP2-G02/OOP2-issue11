from flask import Flask, request, render_template, jsonify
import os, glob

def list_canny():
    name = "static/img/canny_img/"

    return (make_dict(name))


def  list_gray():
    name = "static/img/gray_img/"

    return (make_dict(name))


def  list_binary():
    name = "static/img/binary_img/"

    return (make_dict(name))


def  list_mozaiku():
    name = "static/img/mozaiku_img/"

    return (make_dict(name))
    

def  list_upload():
    name = "static/img/upload_img/"

    return (make_dict(name))


def make_dict(name):
    # ここでdictを作る
    files = []
    img_dict = {}

    # ３種類の拡張子を持つファイルを全部filesに追加していく
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        path = name + ext
        files.extend(glob.glob(path))

    # filesをkey:ファイル名　value：パス名　で作る
    for file in files:
        img_dict[os.path.basename(file)] = file

    # dictを使う理由としては、ファイル名とパス名の両方をhtmlに渡したいため
    return (img_dict)
