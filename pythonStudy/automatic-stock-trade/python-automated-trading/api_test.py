import requests

from dotenv import load_dotenv
import os

print(os.environ)
load_dotenv()

BASE_URL = os.environ["BASE_URL"]
ACCOUNT = os.environ["ACCOUNT"]
APPKEY = os.environ["APPKEY"]
APPSECRET = os.environ["APPSECRET"]

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

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
