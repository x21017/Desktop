import requests
import schedule
import time

def environmental_sensor_data():
    url = 'https://sensor-api.sysken.net/get/sensor'

    try:
        response = requests.get(url)
        response.raise_for_status()  # エラーがあれば例外を発生させる
        sensor_data = response.json()  # JSONレスポンスをPythonのリストに変換
        return sensor_data[:17]  # データを返す
    except requests.exceptions.RequestException as e:
        print("センサーデータを取得できませんでした:", e)
        return None

def job():
    data = environmental_sensor_data()
    if data:
        print("データ:", data)
    else:
        print("データを取得できませんでした")

# 初回の実行
job()

# 10秒ごとにジョブをスケジュール
schedule.every(10).seconds.do(job)

# ループしてスケジュールされたジョブを実行
while True:
    schedule.run_pending()
    time.sleep(1)
