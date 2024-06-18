import requests

BASE_URL = "https://openapivts.koreainvestment.com:29443"
APPKEY="PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
APPSECRET="YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6ImEzNmIzYWUyLTgwNWYtNGYwZS1iMzBiLWNhZThlNjk3YzIzZCIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODc5OTYzOCwiaWF0IjoxNzE4NzEzMjM4LCJqdGkiOiJQUzJaRGFTNG5tdk92Nk1vOER1dFdmVTRuZFk2QUhJNGd5MlcifQ.R28Tu5o8dQGHBo0HYDLBab2WVYfPkr0qtWZPntLeUjO3yNuSecMMi8UbDQSKcw8NMtuMVjRSonmijGVApxif9Q"


def fetch_current_price(code):
    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"
    headers = {
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appkey": APPKEY,
        "appsecret": APPSECRET,
        "tr_id": "FHKST01010100"
    }
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": code
    }
    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()
        return int(data["output"]["stck_prpr"])
    except Exception as e:
        print(e)
        return None

print(fetch_current_price("005930"))