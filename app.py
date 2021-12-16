from flask import Flask, request, render_template
import upload
import list
from werkzeug.utils import secure_filename
from pathlib import Path


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "img" / "upload_img"

@app.route('/')
def index():
    return render_template("index.html")



#POSTの処理
@app.route('/up/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if ("file" in request.files): #存在確認
            f = request.files["the_file"]
            #任意の階層を相対パスで指定
            f.save(UPLOAD_FOLDER / secure_filename(f.filename))
        
    return render_template('index.html')

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)