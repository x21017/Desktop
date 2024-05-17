import requests
import schedule
import time
import subprocess
from datetime import datetime
import pytz

# 日本時間を設定
jst = pytz.timezone('Asia/Tokyo')

# 状態を保持する変数を初期化
condition_met_duration = 0
condition_met = False

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

def staywatch_sensor_data():
    url = 'https://staywatch-backend.kajilab.net/api/v1/stayers'
    try:
        response = requests.get(url)
        response.raise_for_status()  # エラーがあれば例外を発生させる
        staywatch_data = response.json()  # JSONレスポンスをPythonのリストに変換
        return staywatch_data
    except requests.exceptions.RequestException as e:
        print("センサーデータを取得できませんでした:", e)
        return None

def calculate_total_people(staywatch_data):
    total_people = len(staywatch_data)  # 人数をカウント
    return total_people

def play_sounds():
    """音を順番に再生する関数"""
    sound_files = ['ou.mp3', 'male_scream.mp3', 'test.mp3']
    for sound_file in sound_files:
        subprocess.call(['mpg321', sound_file])

def job():
    global condition_met_duration, condition_met
    
    # 現在の日本時間を取得
    now = datetime.now(jst)
    
    # 日本時間での時間帯が10時から18時の間の場合にのみ処理を実行
    if 10 <= now.hour < 18:
        noise_data = environmental_sensor_data()
        staywatch_data = staywatch_sensor_data()
        
        if noise_data is not None and staywatch_data is not None:
            total_people = calculate_total_people(staywatch_data)
            print("取得したデータ: 音量 =", noise_data, ", 人数 =", total_people)
            
            # 条件を確認
            if total_people >= 3 and noise_data <= 90: # 人数が3人以上かつ音量が90以下の時
                if condition_met:
                    condition_met_duration += 5  # 条件が続いている場合は5秒加算
                else:
                    condition_met = True
                    condition_met_duration = 5  # 条件が初めて満たされた場合は10秒に設定
            else:
                condition_met = False
                condition_met_duration = 0  # 条件が満たされていない場合はリセット
            
            # 条件が10秒続いているかを確認
            if condition_met_duration >= 30:
                print("条件が30秒間続いたので音を流します")
                play_sounds()  # 音を順番に再生
                condition_met_duration = 0  # 音を流した後はリセット
        else:
            print("データを取得できませんでした")
            condition_met = False
            condition_met_duration = 0  # エラーの場合もリセット
    else:
        print("時刻が10時を回っていないか、18時を過ぎています")

# 初回の実行
job()

# 50秒ごとにジョブをスケジュール
schedule.every(5).seconds.do(job)

# ループしてスケジュールされたジョブを実行
while True:
    schedule.run_pending()
    time.sleep(1)
