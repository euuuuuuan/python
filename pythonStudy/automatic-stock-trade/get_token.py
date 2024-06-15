import requests

BASE_URL = "https://openapivts.koreainvestment.com:29443"
APPKEY = "PS2ZDaS4nmvOv6Mo8DutWfU4ndY6AHI4gy2W"
APPSECRET = "YtXfq4IY1WhsrXZPi4C2YKdF2bXh/g1c8a2RWv+D7QfMkoK7ReQROFzWqlcsA4+tcjAMim8gpc9IWvCopfek6Hv5cccwf536AHhkvjEpTDkD5HLvlz2G6U2mi3m5rpaDNcf2/rUZi2oiQp4XR4RyhftqfEDvr7JsgMN7Afwky5uePis43ok="

url = f"{BASE_URL}/oauth2/tokenP"
headers = {
    "Content-Type": "application/json"
}
body = {
    "grant_type": "client_credentials",
    "appkey": APPKEY,
    "appsecret": APPSECRET
}
try:
    res = requests.post(url, headers=headers, json=body)
    data = res.json()
    print(data)
except Exception as e:
    print(e)