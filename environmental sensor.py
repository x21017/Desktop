import requests
import subprocess
import schedule
import time

# 気象データを取得して表示する関数
def print_weather_data():
    url = "https://sensor-api.sysken.net/get/sensor"  # 気象APIのURL
    response = requests.get(url)  # リクエストを送信してレスポンスを取得
    weather_data = response.json()  # レスポンスからJSONデータを取得
    
    # 必要な属性を取得
    id = weather_data["id"]
    time_measured = weather_data["time_measured"]
    area_id = weather_data["area_id"]
    temperature = weather_data["temperature"]
    relative_humidity = weather_data["relative_humidity"]
    ambient_light = weather_data["ambient_light"]
    barometric_pressure = weather_data["barometric_pressure"]
    sound_noise = weather_data["sound_noise"]
    eTVOC = weather_data["eTVOC"]
    eCO2 = weather_data["eCO2"]
    discomfort_index = weather_data["discomfort_index"]
    heat_stroke = weather_data["heat_stroke"]
    vibration_information = weather_data["vibration_information"]
    si_value = weather_data["si_value"]
    pga = weather_data["pga"]
    seismic_intensity = weather_data["seismic_intensity"]
    date = weather_data["date"]

    # 取得した値を表示
    print("ID:", id)
    print("Time Measured:", time_measured)
    print("Area ID:", area_id)
    print("Temperature:", temperature)
    print("Relative Humidity:", relative_humidity)
    print("Ambient Light:", ambient_light)
    print("Barometric Pressure:", barometric_pressure)
    print("Sound Noise:", sound_noise)
    print("eTVOC:", eTVOC)
    print("eCO2:", eCO2)
    print("Discomfort Index:", discomfort_index)
    print("Heat Stroke:", heat_stroke)
    print("Vibration Information:", vibration_information)
    print("SI Value:", si_value)
    print("PGA:", pga)
    print("Seismic Intensity:", seismic_intensity)
    print("Date:", date)

# 定期的に気象データを取得して表示する
schedule.every(10).seconds.do(print_weather_data)

# メインループ
while True:
    schedule.run_pending()
    time.sleep(1)
