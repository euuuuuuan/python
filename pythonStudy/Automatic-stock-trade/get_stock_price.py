import requests

BASE_URL = "https://openapivts.koreainvestment.com:29443"
APPKEY = "PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
APPSECRET = "YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjA2MjU5NDRmLWU2NjAtNDY0NC05MzQwLTU3ZmZkMmJiMjQ4YyIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTcxODUxODA5OSwiaWF0IjoxNzE4NDMxNjk5LCJqdGkiOiJQUzJaRGFTNG5tdk92Nk1vOER1dFdmVTRuZFk2QUhJNGd5MlcifQ.d322X3nEPBGQMuWZ2TtojaBO1AP1pcv6N-9iG787tc6QoaenUkoiEO5yv7zxQQCgmoPgHhJXjMTfuRQNbNzmsg"

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
    print(data["output1"]["hts_kor_isnm"])  # HTS 한글 종목명
    for item in data["output2"]:
        print(f"시간: {item['stck_bsop_date']} {item['stck_cntg_hour']} 가격:{item['stck_prpr']}")
except Exception as e:
    print(e)