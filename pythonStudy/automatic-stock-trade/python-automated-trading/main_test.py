# main.py 자동 매매
import requests
from time import sleep
from backtest_test import calculate_moving_average, generate_signals

# API로 현재 가격을 가져오는 함수
def get_current_price(symbol, appkey, appsecret, access_token):
    BASE_URL = "https://openapivts.koreainvestment.com:29443"
    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {access_token}",
        "appkey": appkey,
        "appsecret": appsecret,
        "tr_id": "FHKST03010200",
        "custtype": "P"
    }
    params = {
        "FID_ETC_CLS_CODE": "",
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": symbol,
        "FID_INPUT_HOUR_1": "093000",
        "FID_PW_DATA_INCU_YN": "Y"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

# 초기 설정
symbol = "005930"  # 삼성전자 종목 코드
appkey = "PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
appsecret = "YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6Ijk5MmNjYTU1LTYxMzItNDZiYy04YjViLWJjM2RmMTEyMWU3NSIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODcxNDg4NCwiaWF0IjoxNzE4NjI4NDg0LCJqdGkiOiJQUzJaRGFTNG5tdk92Nk1vOER1dFdmVTRuZFk2QUhJNGd5MlcifQ.S90bgEquXF6xpIuo74ir8iCujkP986IXq1a5dzSc7tp4MUqi3Gi_Jwham2AbWltK1OpAb0ejEx5P3o3ix4aA-g"

balance = 10000000  # 초기 잔고 설정
stocks = 0  # 보유 주식 수
prices = []  # 가격 기록

while True:
    try:
        current_data = get_current_price(symbol, appkey, appsecret, access_token)
        price_data = current_data.get("output2", [])  # output2에서 가격 데이터 가져오기

        if len(price_data) > 0:
            current_price = float(price_data[0].get("stck_prpr", 0))  # 가장 최근의 가격 가져오기
            prices.append(current_price)

            if len(prices) >= 60:  # 최소 60개의 가격 데이터 필요
                ma20 = calculate_moving_average(prices, 20)
                ma60 = calculate_moving_average(prices, 60)
                signals = generate_signals(ma20, ma60)
                signal = signals[-1]

                if signal == "Buy" and balance >= current_price:
                    stocks += balance // current_price
                    balance -= stocks * current_price
                    print(f"Buying at {current_price}, Balance: {balance}, Stocks: {stocks}")
                elif signal == "Sell" and stocks > 0:
                    balance += stocks * current_price
                    stocks = 0
                    print(f"Selling at {current_price}, Balance: {balance}, Stocks: {stocks}")

        sleep(60)  # 1분마다 반복

    except Exception as e:
        print(e)
        sleep(60)  # 에러 발생 시에도 1분 대기
