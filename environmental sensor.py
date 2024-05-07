import requests
import schedule
import time
import schedule
import subprocess

def environmental_sensor_data():
    url = 'https://sensor-api.sysken.net/get/sensor'

    try:
        response = requests.get(url)
        response.raise_for_status()  # エラーがあれば例外を発生させる
        sensor_data = response.json()  # JSONレスポンスをPythonのリストに変換
        return sensor_data[0]['temperature']
    except requests.exceptions.RequestException as e:
        print("センサーデータを取得できませんでした:", e)
        return None

def job():
    data = environmental_sensor_data()
    if data:
        # print(len(data))
        print("取得したデータ:", data)
        # print("温度:", data)
    else:
        print("データを取得できませんでした")
# 温度の閾値によって音楽を流す
    # if data >= 26:
    #     print("温度が26度以上です.")
    #     subprocess.Popen(['mpg321', 'test.mp3'])
    # else:
    #     print("温度は26度以下です") 

# 初回の実行
job()

# 10秒ごとにジョブをスケジュール
schedule.every(10).seconds.do(job)

# ループしてスケジュールされたジョブを実行
while True:
    schedule.run_pending()
    time.sleep(1)
