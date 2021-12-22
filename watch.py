import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from cv_lib import main

#イベントハンドラ
class ChangeHandler(FileSystemEventHandler):

    #ファイルやフォルダが作成された場合
    def on_created(self, event):
        filepath = event.src_path
        print('filepath : ',filepath)

        filename = os.path.basename(filepath)
        print('filename : ',filename)

        main.start_opencv(filepath) #main.py 呼び出し
        print('%sを作成しました。' % filename)

    '''#ファイルやフォルダが更新された場合
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        main.start_opencv()
        print('%sを変更しました。' % filename)

    #ファイルやフォルダが移動された場合
    def on_moved(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        main.start_opencv()
        print('%sを移動しました。' % filename)

    #ファイルやフォルダが削除された場合
    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        main.start_opencv()
        print('%sを削除しました。' % filename)'''

if __name__ == "__main__":
    #ロギングの設定
    '''logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')'''
    
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'    #監視対象のpathを設定

    path = "./static/img/upload_img"                            #監視対象のpathを設定

    #event_handler = LoggingEventHandler()                #イベントハンドラ生成
    event_handler = ChangeHandler()

    observer = Observer()       #監視オブジェクト生成
    observer.schedule(event_handler,path,recursive=True) #監視設定
    print("hello")              #動作確認

    observer.start()            #監視開始
    try:
        while True:             #ctrl-Cが押されるまで実行
            time.sleep(1)       #1秒停止
    except KeyboardInterrupt:   #ctrl-C実行時
        observer.stop()         #監視修了
    observer.join()