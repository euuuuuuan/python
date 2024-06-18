from time import sleep
import requests

BASE_URL = "https://openapivts.koreainvestment.com:29443"
APPKEY="PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
APPSECRET="YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6ImEzNmIzYWUyLTgwNWYtNGYwZS1iMzBiLWNhZThlNjk3YzIzZCIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODc5OTYzOCwiaWF0IjoxNzE4NzEzMjM4LCJqdGkiOiJQUzJaRGFTNG5tdk92Nk1vOER1dFdmVTRuZFk2QUhJNGd5MlcifQ.R28Tu5o8dQGHBo0HYDLBab2WVYfPkr0qtWZPntLeUjO3yNuSecMMi8UbDQSKcw8NMtuMVjRSonmijGVApxif9Q"
CODE = "005930"

def ma(values, window_size):
    if len(values) >= window_size:
        target_values = values[-window_size:]
        return sum(target_values) / window_size
    else:
        return None

def ma_signal(ma_short_term, ma_long_term):
    if len(ma_short_term) < 2 or len(ma_long_term) < 2:
        return None
    if None in ma_short_term[-2:] or None in ma_long_term[-2:]:
        return None
    prev = ma_short_term[-2] - ma_long_term[-2]
    current = ma_short_term[-1] - ma_long_term[-1]

    if prev < 0 and current >= 0:
        return "BUY"
    elif prev >= 0 and current < 0:
        return "SELL"
    else:
        return None

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
    res = requests.get(url, headers=headers, params=params)
    try:
        data = res.json()
        return int(data["output"]["stck_prpr"])
    except Exception as e:
        print(e)
        return None

def clear_orders():
    return

def fetch_avail():
    return 0

def fetch_quantity():
    return 0

def order():
    return

# 자동 매매 코드

prices = []
ma20 = []
ma60 = []

while True:
    # 현재 가격 조회
    current_price = fetch_current_price("005930")
    if current_price is not None:
        prices.append(current_price)
        # 이동 평균선 계산
        ma20.append(ma(prices, 20))
        ma60.append(ma(prices, 60))
        # 투자 전략 확인
        signal = ma_signal(ma20, ma60)
        print(
            f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
        # 과거 주문을 조회하고 미체결된 주문이 있으면 취소하기
        clear_orders()

        # 전략에 따라 주문하기
        amount = 0
        if signal == "BUY":
            # 매수 주문 가능한 수량 조회하기
            amount = fetch_avail()
        elif signal == "SELL":
            # 보유 수량 업데이트하기
            amount = fetch_quantity()
        if amount > 0:
            order()
    sleep(60)