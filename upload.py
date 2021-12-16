from flask import Flask, request, render_template, jsonify
import os, glob

def list():
    import glob

    files = glob.glob("static/img/canny_img/*.jpg")
    print(files)
    
    return (files)


if __name__ == "__main__":
    list()

    