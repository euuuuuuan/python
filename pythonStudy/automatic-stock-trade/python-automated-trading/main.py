# 1분에 한 번씩 주식의 현재가를 가져옵니다.
# 이동 평균값을 계산해서 매매 전략에 따라 전량 매수, 전량 매도를 합니다.
# 필요하다면 거래 성공 여부 등을 출력합니다.
# 필요하다면 수익률을 확인하기 위해서 현재 잔고의 총 평가금액을 출력합니다.

# 2. 자동 매매 구현하기
# # 우선 API로 현재 가격을 가져오는 함수를 작성해 보세요.
# #
# # while 반복문과 time 모듈의 sleep() 함수를 사용해서 1분마다 반복하는 코드를 작성합니다.
#
# 실제 API 리퀘스트를 보내는 함수를 작성해 보고, 이 함수를 while 반복문에 반영해 봅니다.

import requests
from time import sleep


# 함수 : 이동 평균선 값 계산
def calculate_moving_average(price, window_size):
    moving_averages = []
    for i in range(window_size, len(price)):
        avg = sum(price[i - window_size:i]) / window_size
        moving_averages.append(avg)
    return moving_averages


balance = 10000000  # 초기 잔고 설정
stocks = 0  # 보유 주식 수
prices = []  # 가격 기록
while True:
    BASE_URL = "https://openapivts.koreainvestment.com:29443"
    APPKEY = "PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
    APPSECRET = "YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="
    ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6Ijk5MmNjYTU1LTYxMzItNDZiYy04YjViLWJjM2RmMTEyMWU3NSIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODcxNDg4NCwiaWF0IjoxNzE4NjI4NDg0LCJqdGkiOiJQUzJaRGFTNG5tdk92Nk1vOER1dFdmVTRuZFk2QUhJNGd5MlcifQ.S90bgEquXF6xpIuo74ir8iCujkP986IXq1a5dzSc7tp4MUqi3Gi_Jwham2AbWltK1OpAb0ejEx5P3o3ix4aA-g"

    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appkey": APPKEY,
        "appsecret": APPSECRET,
        "tr_id": "FHKST03010200",
        "custtype": "P"
    }
    params = {
        "FID_ETC_CLS_CODE": "",
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": "005930",
        "FID_INPUT_HOUR_1": "093000",
        "FID_PW_DATA_INCU_YN": "Y"
    }
    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()
        print(data["output1"]["hts_kor_isnm"])
        price_data = data["output2"]["stck_prpr"]
        print(price_data)
        moving_average_20 = calculate_moving_average(price_data, 20)
        moving_average_60 = calculate_moving_average(price_data, 60)
        print("20일 주식 이동 평균:", moving_average_20)
        print("60일 주식 이동 평균:", moving_average_60)
        for item in data["output2"]:
            print(f"시간: {item['stck_bsop_date']} {item['stck_cntg_hour']} 가격:{item['stck_prpr']}")
    except Exception as e:
        print(e)

    sleep(60)

# while True:
#     BASE_URL = "https://openapivts.koreainvestment.com:29443"
#     APPKEY = "PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
#     APPSECRET = "YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="
#
#     ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6Ijk5MmNjYTU1LTYxMzItNDZiYy04YjViLWJjM2RmMTEyMWU3NSIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODcxNDg4NCwiaWF0IjoxNzE4NjI4NDg0LCJqdGkiOiJQUzJaRGFTNG5tdk92Nk1vOER1dFdmVTRuZFk2QUhJNGd5MlcifQ.S90bgEquXF6xpIuo74ir8iCujkP986IXq1a5dzSc7tp4MUqi3Gi_Jwham2AbWltK1OpAb0ejEx5P3o3ix4aA-g"
#
#     url = f"{BASE_URL}//oauth2/tokenP"
#     res = requests.post(url)
#     hearders = {
#         "Content-Type": "application/json; charset=UTF-8"}
#     body = {
#         "grant_type": "client_credentials",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET
#     }
#     try:
#         res = requests.post(url, headers=hearders, json=body)
#         data = res.json()
#         print(data)
#     except Exception as e:
#         print(e)
#     # 1분마다 실행할 코드
#     sleep(60)

# sleep 함수는 파이썬의 time 모듈에서 제공하는 함수입니다.
# 이 함수는 프로그램의 실행을 일정 시간 동안 멈추게 만듭니다.
# 즉, 코드의 실행을 지정된
# 시간(초 단위) 동안 일시적으로 정지시키는 역할을 합니다.
#
# 여기서 from time import sleep은 time 모듈에서
# sleep 함수만을 가져온다는 의미입니다.
# 이렇게 하면 time.sleep() 대신 sleep() 함수를
# 직접 사용할 수 있습니다.
#
# 예를 들어, 위의 코드에서는 while True: 루프를 사용하여
# 무한 반복하면서, 1분마다 특정 코드를 실행하고자 합니다.
# sleep(60)은 60초(즉, 1분) 동안 프로그램의 실행을 멈추게 하며,
# 그 후에 다시 반복문의 시작으로 돌아가서 코드를 실행합니다.
