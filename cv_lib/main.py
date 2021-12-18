from . import canny
from . import gray

def start_opencv(path):
    print("start_opencv...")

    # それぞれの画像処理を実行
    canny.canny(path)
    gray.gray(path)