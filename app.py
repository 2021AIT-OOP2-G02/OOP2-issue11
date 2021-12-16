from flask import Flask, request, render_template
import os
import upload
import list
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#GETの処理
@app.route('/up/', methods=['GET'])
def up_get():
    return render_template('index.html', message = '画像を選択しよう', flag = False)

#POSTの処理
@app.route('/up/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files["the_file"]
        #任意の階層をフルパスで指定(macの場合。任意のユーザー名は変更してください。)
        f.save('/Users/任意のユーザー名/Python/myproject/uploads/' + secure_filename(f.filename))
        #アップロードしてサーバーにファイルが保存されたらfinishedを表示
        return render_template('finished.html')
    else:
    	#GETでアクセスされた時、uploadsを表示
    	return render_template('uploads.html')