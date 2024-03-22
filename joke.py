import requests

# ダジャレを取得する関数
def joke():
    url = "https://icanhazdadjoke.com/"  # ジョークAPIのURL
    headers = {"Accept": "application/json"}  # JSON形式のデータを要求するヘッダー
    response = requests.get(url, headers=headers)  # リクエストを送信してレスポンスを取得
    joke_data = response.json()  # レスポンスからJSONデータを取得
    return joke_data["joke"]  # ジョークを返す


# この関数を呼び出してジョークを取得することができます



if __name__ == '__main__':
    print(joke())