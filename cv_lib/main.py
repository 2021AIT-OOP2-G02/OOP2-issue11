from . import canny
from . import gray
from . import mozaiku

def start_opencv(path):
    print("start_opencv...")

    # それぞれの画像処理を実行
    canny.canny(path)
    gray.gray(path)
    mozaiku.rectangle(path)
    mozaiku.mozaiku(path)
