import requests
import subprocess
import schedule
import time

# ジョークを取得する関数
def joke():
    url = "https://sensor-api.sysken.net/get/sensor"  # ジョークAPIのURL
    headers = {"Accept": "application/json"}  # JSON形式のデータを要求するヘッダー
    response = requests.get(url, headers=headers)  # リクエストを送信してレスポンスを取得
    joke_data = response.json()  # レスポンスからJSONデータを取得
    return joke_data["id"], joke_data["time_measured"], joke_data["area_id"], joke_data["temperature"], joke_data["relative_humidity"],joke_data["ambient_light"], joke_data["barometric_pressure"], joke_data["sound_noise"], joke_data["eTVOC"], joke_data["eCO2"], joke_data["discomfort_index"], joke_data["heat_stroke"], joke_data["vibration_information"], joke_data["si_value"], joke_data["pga"], joke_data["seismic_intensity"], joke_data["date"]  # ジョークとIDを返す


# この関数を呼び出してジョークとIDを取得する
def print_joke_and_play_sound():
    id = joke()
    print("id:", id)
    
    if id % 2 == 0:
        print("Playing male scream sound...")
        subprocess.Popen(['mpg321', 'male_scream.mp3'])
    else:
        print("Playing 'Ou!' sound...")
        subprocess.Popen(['mpg321', 'ou.mp3'])

# 定期的にジョークを取得し、効果音を再生する
schedule.every(10).seconds.do(print_joke_and_play_sound)

# メインループ
while True:
    schedule.run_pending()
    time.sleep(1)
