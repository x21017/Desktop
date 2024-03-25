import requests

# ジョークを取得する関数
def joke():
    url = "https://official-joke-api.appspot.com/jokes/random"  # ジョークAPIのURL
    headers = {"Accept": "application/json"}  # JSON形式のデータを要求するヘッダー
    response = requests.get(url, headers=headers)  # リクエストを送信してレスポンスを取得
    joke_data = response.json()  # レスポンスからJSONデータを取得
    return joke_data["setup"], joke_data["punchline"], joke_data["id"]  # ジョークとIDを返す


# この関数を呼び出してジョークとIDを取得する
if __name__ == '__main__':
    setup, punchline, id = joke()
    print("Setup:", setup)
    print("Punchline:", punchline)
    print("Id", id)
