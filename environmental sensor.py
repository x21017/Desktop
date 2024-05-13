import requests
import schedule
import time
import subprocess
from datetime import datetime
import pytz

# 日本時間のタイムゾーンを設定
jst = pytz.timezone('Asia/Tokyo')

def environmental_sensor_data():
    url = 'https://sensor-api.sysken.net/get/sensor'

    try:
        response = requests.get(url)
        response.raise_for_status()  # エラーがあれば例外を発生させる
        sensor_data = response.json()  # JSONレスポンスをPythonのリストに変換
        return sensor_data[0]['sound_noise']
    except requests.exceptions.RequestException as e:
        print("センサーデータを取得できませんでした:", e)
        return None

def job():
    # 現在の日本時間を取得
    now = datetime.now(jst)
    
    # 日本時間での時間帯が10時から18時の間の場合にのみ処理を実行
    if 10 <= now.hour < 18:
        data = environmental_sensor_data()
        if data:
            print("取得したデータ:", data)
            # 音量の閾値によって音楽を流す
            if data >= 30:
                print("部屋の中が静かです.")
                subprocess.Popen(['mpg321', 'test.mp3'])
        else:
            print("データを取得できませんでした")
    else:
        print("時刻が18時を過ぎています")

# 初回の実行
job()

# 10秒ごとにジョブをスケジュール
schedule.every(10).seconds.do(job)

# ループしてスケジュールされたジョブを実行
while True:
    schedule.run_pending()
    time.sleep(1)
