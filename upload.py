from flask import Flask, request, render_template, jsonify
import os, glob

def list_canny():
    files = glob.glob("static/img/canny_img/*.jpg")
    print(type(files))
    return (files)


def  list_gray():
    files = glob.glob("static/img/gray_img/*.jpg")
    return (files)


def  list_mozaiku():
    files = glob.glob("static/img/mozaiku_img/*.jpg")
    return (files)

def  list_upload():
    files = glob.glob("static/img/upload_img/*.jpg")
    return (files)

