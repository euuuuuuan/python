# 이번 레슨에서는 마지막으로 이렇게 작성한 코드를 개선할 수 있는 여러 가지 방법에 대해 소개해 드릴게요. 앞으로 어떤 내용을 더 찾아보거나 공부하면 좋을지 고민이라면, 이 내용을 참고해서 방향을 잡아 보셔도 좋을 것 같습니다.
#
# 모듈로 코드 재사용하기
# 앞에서 작성했던 코드들 중에 ma() 함수나 ma_signal() 함수는 backtest.py 파일에서도 사용하고 main.py 파일에서도 사용했었습니다. 이런 경우 파일을 분리하고 재사용하면 좋은데요.
#
# 예를 들어서 아래와 같이 indicator.py라는 파일이랑 strategy.py라는 파일을 만든다고 해 볼게요. 그리고 API 리퀘스트를 보내는 함수들도 모아서 api.py라는 파일에 옮길 수도 있을 겁니다.
#
#  indicator.py
#
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
#  strategy.py {% filename %}
#
#
# def ma_signal(ma_short_term, ma_long_term):
#     if len(ma_short_term) < 2 or len(ma_long_term) < 2:
#         return None
#     if None in ma_short_term[-2:] or None in ma_long_term[-2:]:
#         return None
#     prev = ma_short_term[-2] - ma_long_term[-2]
#     current = ma_short_term[-1] - ma_long_term[-1]
#
#     if prev < 0 and current >= 0:
#         return "BUY"
#     elif prev >= 0 and current < 0:
#         return "SELL"
#     else:
#         return None
#  api.py
#
#
# import requests
# from datetime import datetime
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# ACCOUNT = "..."
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
#
# def fetch_current_price(code):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "FHKST01010100"
#     }
#     params = {
#         "FID_COND_MRKT_DIV_CODE": "J",
#         "FID_INPUT_ISCD": code
#     }
#     res = requests.get(url, headers=headers, params=params)
#     try:
#         data = res.json()
#         return int(data["output"]["stck_prpr"])
#     except Exception as e:
#         print(e)
#         return None
#
# def fetch_orders(account, code):
#     today = datetime.today().strftime('%Y%m%d')
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/inquire-daily-ccld"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "VTTC8001R"
#     }
#     params = {
#         "CANO": account[:8],
#         "ACNT_PRDT_CD": account[-2:],
#         "INQR_STRT_DT": today,
#         "INQR_END_DT": today,
#         "SLL_BUY_DVSN_CD": "00",
#         "INQR_DVSN": "00",
#         "PDNO": code,
#         "CCLD_DVSN": "02",  # 미체결
#         "ORD_GNO_BRNO": "",
#         "ODNO": "",
#         "INQR_DVSN_3": "00",
#         "INQR_DVSN_1": "",
#         "CTX_AREA_FK100": "",
#         "CTX_AREA_NK100": ""
#     }
#
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         return data["output1"]
#     except Exception as e:
#         print(e)
#         return []
#
# def cancel_order(account, order_no):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/order-rvsecncl"
#     headers = {
#         "content-type": "application/json; charset=utf-8",
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "VTTC0803U"
#     }
#     body = {
#         "CANO": account[:8],
#         "ACNT_PRDT_CD": account[-2:],
#         "KRX_FWDG_ORD_ORGNO": "",
#         "ORGN_ODNO": order_no,
#         "ORD_DVSN": "00",
#         "RVSE_CNCL_DVSN_CD": "02",  # 취소
#         "ORD_QTY": "0",  # 잔량전부 취소
#         "ORD_UNPR": "0",  # 취소
#         "QTY_ALL_ORD_YN": "Y",  # 잔량 전부
#     }
#
#     try:
#         res = requests.post(url, headers=headers, json=body)
#         data = res.json()
#         return data["rt_cd"] == "0"
#     except Exception as e:
#         print(e)
#         return False
#
# def clear_orders(account, code):
#     orders = fetch_orders(account, code)
#     for order in orders:
#         order_no = order["odno"]
#         result = cancel_order(account, order_no)
#         print(f"{order_no} 취소 성공" if result else f"{order_no} 취소 실패")
#
# def fetch_avail(account, code, target_price):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/inquire-psbl-order"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "VTTC8908R"
#     }
#     params = {
#         "CANO": account[:8],
#         "ACNT_PRDT_CD": account[-2:],
#         "PDNO": code,
#         "ORD_UNPR": str(target_price),
#         "ORD_DVSN": "00",  # 지정가
#         "CMA_EVLU_AMT_ICLD_YN": "N",
#         "OVRS_ICLD_YN": "N",
#     }
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         return data["output"]["nrcvb_buy_qty"]  # 미수 없는 매수 가능 수량
#     except Exception as e:
#         print(e)
#         return 0
#
# def fetch_quantity(account, code):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/inquire-balance"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "VTTC8434R"  # 주식 잔고 조회
#     }
#     params = {
#         "CANO": account[:8],
#         "ACNT_PRDT_CD": account[-2:],
#         "AFHR_FLPR_YN": "N",
#         "INQR_DVSN": "02",  # 종목별
#         "UNPR_DVSN": "01",  # 단가 구분 기본값
#         "FUND_STTL_ICLD_YN": "N",
#         "FNCG_AMT_AUTO_RDPT_YN": "N",
#         "PRCS_DVSN": "00",  # 전일 매매 포함
#         "CTX_AREA_FK100": "",
#         "CTX_AREA_NK100": ""
#     }
#
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         for item in data["output1"]:
#             if item["pdno"] == code:
#                 return item["hldg_qty"]
#         return 0
#     except Exception as e:
#         print(e)
#         return 0
#
# def order(order_type, account, code, amount, target_price):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/order-cash"
#     headers = {
#         "content-type": "application/json; charset=utf-8",
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "VTTC0802U" if order_type == "BUY" else "VTTC0801U"  # 주식 현금 매수/매도 주문
#     }
#     body = {
#         "CANO": account[:8],
#         "ACNT_PRDT_CD": account[-2:],
#         "PDNO": code,
#         "ORD_DVSN": "00",  # 지정가
#         "ORD_QTY": str(amount),
#         "ORD_UNPR": str(target_price)
#     }
#
#     try:
#         res = requests.post(url, headers=headers, json=body)
#         data = res.json()
#         return data["rt_cd"] == 0
#     except Exception as e:
#         print(e)
#         return False
#
# def fetch_eval(account):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/inquire-balance"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "VTTC8434R"  # 주식 잔고 조회
#     }
#     params = {
#         "CANO": account[:8],
#         "ACNT_PRDT_CD": account[-2:],
#         "AFHR_FLPR_YN": "N",
#         "OFL_YN": "",  # 공란
#         "INQR_DVSN": "02",  # 종목별
#         "UNPR_DVSN": "01",  # 단가 구분 기본값
#         "FUND_STTL_ICLD_YN": "N",
#         "FNCG_AMT_AUTO_RDPT_YN": "N",
#         "PRCS_DVSN": "00",  # 전일 매매 포함
#         "CTX_AREA_FK100": "",
#         "CTX_AREA_NK100": ""
#     }
#
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         print(data)
#         return data["output2"][0]["tot_evlu_amt"]
#     except Exception as e:
#         print(e)
#         return None
#
# 그럼 이 파일들을 backtest.py랑 main.py 에서 불러와서 쓸 수 있겠죠?
#
#  backtest.py
#
#
# import json
# import indicator
# import strategy
#
# def load_prices(filename):
#     data = {}
#     result = []
#
#     with open(filename, "r") as f:
#         data = json.load(f)
#         f.close()
#     for item in data:
#         current_price = int(item["stck_prpr"])
#         result.append(current_price)
#
#     return result
#
# def backtest(prices, initial_balance):
#     balance = initial_balance
#     quantity = 0
#     ma20 = []
#     ma60 = []
#
#     for i in range(len(prices)):
#         ma20.append(indicator.ma(prices[:i], 20))
#         ma60.append(indicator.ma(prices[:i], 60))
#         signal = strategy.ma_signal(ma20, ma60)
#
#         if signal == "BUY":
#             amount = balance // prices[i]  # 전량 매수
#             quantity += amount
#             balance -= amount * prices[i]
#         elif signal == "SELL":
#             amount = quantity  # 전량 매도
#             quantity -= amount
#             balance += amount * prices[i]
#
#         # 현재 수익률(%)
#         roi = ((balance + prices[i] * quantity) / initial_balance - 1) * 100
#         if signal is not None:
#             print(f"시그널: {signal} 수익률: {roi}%")
#
# sample_prices = load_prices("sample.json")
# backtest(sample_prices, 1000 * 10000)
#
#  main.py
#
#
# from time import sleep
# import indicator
# import strategy
# import api
#
# CODE = "005930"
#
# # 자동 매매 코드
#
# prices = []
# ma20 = []
# ma60 = []
#
# while True:
#     # 현재 가격 조회
#     current_price = api.fetch_current_price("005930")
#     if current_price is not None:
#         prices.append(current_price)
#         # 이동 평균선 계산
#         ma20.append(indicator.ma(prices, 20))
#         ma60.append(indicator.ma(prices, 60))
#         # 투자 전략 확인
#         signal = strategy.ma_signal(ma20, ma60)
#         print(
#             f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
#         # 과거 주문을 조회하고 미체결된 주문이 있으면 취소하기
#         api.clear_orders(ACCOUNT, CODE)
#
#         # 전략에 따라 주문하기
#         amount = 0
#         if signal == "BUY":
#             # 매수 주문 가능한 수량 조회하기
#             amount = api.fetch_avail(ACCOUNT, CODE, prices[-1])
#         elif signal == "SELL":
#             # 보유 수량 업데이트하기
#             amount = api.fetch_quantity(ACCOUNT, CODE)
#         if amount > 0:
#             result = api.order(signal, ACCOUNT, CODE, amount, prices[-1])
#             if result:
#                 print(f"{signal} {CODE} {amount}개 {prices[-1]}원 주문 성공")
#     eval = api.fetch_eval(ACCOUNT)
#     print(f"총 평가금: {eval}")
#     sleep(60)
#
# 환경 변수로 안전하게 코딩하기
# 앞에서 보안상 중요한 값들을 꽤 많이 사용했었습니다. 예를 들면 APPKEY, APPSECRET 그리고 계좌 번호에 해당하는 ACCOUNT 같은 값을 파이썬 코드에 변수로 정의하고 썼는데요. 사실 이런 값들은 되도록이면 소스 코드 파일에 저장하지 않는 게 좋습니다.
#
# 프로그래밍 분야에서는 이럴 때 "환경 변수"라는 걸 써요. 쉽게 말해서 변수는 변수인데, 환경에 달라지는 변수라고 보시면 되는데요. 예를 들어서 어떤 프로그램을 쓴다고 했을 때 Windows 사용자 이름 같은 걸 보여 주는 거 보신 적 있나요? 이런 건 내가 입력한 적도 없고 Windows를 쓰는 컴퓨터마다 사용자 이름이 다를 텐데 프로그램에서 보여 주는 값입니다. 이런 값들이 환경 변수인데요. 내 컴퓨터에 환경 변수 값으로 어떤 값들이 저장돼 있으면 프로그램을 실행할 때 그 환경 변수 값을 불러와서 쓰는 겁니다. 그래서 똑같은 프로그램이라도 서로 다른 컴퓨터에서 다른 값을 쓸 수가 있어요.
#
# 특히 비밀번호나 계좌 번호같이 보안상 중요한 값은 소스 코드에 포함시켜선 안 됩니다.
#
# 파이썬 코드에서도 환경 변수를 쓰는 방법이 있어요. 파이썬에서는 운영 체제를 다루는 os라는 모듈이 있는데요. os.environ이라는 값으로 환경 변수 값을 불러올 수 있습니다. 이 값은 사전으로 돼 있어요. 아래 코드를  여러 컴퓨터에서 실행해 보시면 각 컴퓨터마다 다른 값이 보일 겁니다.
#
#
# import os
#
# print(os.environ)
# 만약에 환경 변수 중에서 USER라는 이름의 값을 가져오고 싶다. 그럼 이렇게 사용하면 됩니다. 쉽죠?
#
#
# os.environ["USER"]
# 문제는 환경 변수를 저장하는 방법입니다. 환경 변수를 설정하는 건 꽤나 번거로운 일인데요. 그래서 최근에는 코드 실행에 필요한 환경 변수 값들은 소스 코드랑 분리해서 . env라는 이름의 숨김 파일로 저장하는 추세입니다. dotenv(닷인브)라고 부르는 파일인데, 예를 들면 앞에서 썼던 APPKEY, APPSECRET, ACCOUNT 값은 아래처럼 저장해 놓고 쓸 수 있어요.
#
#  .env
#
#
# APPKEY=...
# APPSECRET=...
# ACCOUNT=...
# 파이썬 코드에서는 이 값을 아래처럼 불러와서 쓰면 됩니다. 이때 python-dotenv라는 모듈이 필요해요. load_dotenv()라는 함수로 .env 파일을 불러와서 환경 변수 값을 집어넣는 방식입니다.
#
#
#
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# ...
#
# APPKEY = os.environ["APPKEY"]
# APPSECRET = os.environ["APPSECRET"]
# ACCOUNT = os.environ["ACCOUNT"]
#
# ...
#
# 이렇게 코드를 개선하면 소스 코드를 다른 사람과 공유해도 수정할 필요가 없고, 각자 .env 파일만 보안에 유의하면서 만들어서 쓰면 되니까 편리하겠죠?
#
# Pandas로 편하게 계산하기
# 앞에서 이동 평균선을 구하는 함수 기억나시나요?
#
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
#
# def test(prices):
#     ma20 = []
#     ma60 = []
#     for i in range(len(prices)):
#         ma20.append(ma(prices[:i], 20))
#         ma60.append(ma(prices[:i], 60))
#         ...
#
#
# prices = [...]
# test(prices)
# ma()라는 함수는 리스트와 숫자를 파라미터로 받아서 이동 평균값을 계산해 주죠. 20, 60이라는 값에 재활용할 수 있도록 만들긴 했지만 코드가 너무 복잡한 느낌이 있습니다.
#
# 파이썬에서는 복잡한 숫자 계산을 할 때 주로 Pandas라는 라이브러리를 사용합니다. 이걸 사용하면 복잡한 계산도 짧은 코드로 할 수 있는데요. 리스트를 DataFrame이라는 데이터형으로 바꿔 놓으면, Pandas에서 제공하는 여러 함수로 복잡한 계산을 편리하게 할 수 있습니다.
#
#
# import pandas as pd
#
# def test(df):
#     ma20 = df.rolling(20).mean()
#     ma60 = df.rolling(60).mean()
#     ...
#
# df_prices = pd.DataFrame([...])
# test(df_prices)
# Pandas는 데이터 사이언스, 머신 러닝 등 다양한 분야에서 거의 필수적으로 활용하는 라이브러리예요. 파이썬을 배우고 나서 다음 단계로 뭘 배울지 고민인 분들이라면 무조건 추천하는 기술입니다.
#
# 코드잇에서는 [데이터 분석, 기초에서 실전까지] 로드맵에서 Pandas를 다루는 커리큘럼을 제공하고 있으니 한번 살펴보셔도 좋습니다.
#
# 이걸 배우면서 재미를 느끼신다면 [데이터 사이언티스트] 로드맵이나 [머신 러닝] 로드맵에 도전해 볼 수도 있겠죠?
#
# Matplotlib으로 그래프 그리기
# 앞에서 백테스팅을 할 때 텍스트로만 결과를 출력해 보고 판단했었는데요. 이것 때문에 답답하셨던 분들도 있을 겁니다. 파이썬에서는 간편하게 그래프를 그리는 용도로 Matplotlib이라는 걸 써요. 이 라이브러리를 사용하면 파이썬 데이터로 다양한 그래프를 그리고, 간단하게 인사이트를 도출해 낼 수 있습니다.
#
# 예를 들면 앞에서 작성한 백테스트를 조금 수정해서 show_graph()라는 함수를 만들고, 수익률 데이터도 interests라는 리스트에 모은 다음 이걸 한 그래프에 그려 보면 다음과 같이 가격 변화와 이동 평균선, 매수 신호와 매도 신호 그리고 수익률을 시각적으로 확인할 수 있어요.
#
#
# import json
# import matplotlib.pyplot as plt
#
# ...
#
# def show_graph(prices, ma20, ma60, interests):
#     _, ax1 = plt.subplots()
#     ax1.plot(range(len(prices)), prices, label="가격", color="black")
#     ax1.plot(range(len(ma20)), ma20, label="ma20", color="orange")
#     ax1.plot(range(len(ma60)), ma60, label="ma60", color="yellow")
#     for i in range(len(prices)):
#         y = prices[i]
#         signal = ma_signal(ma20[:i], ma60[:i])
#         if signal is not None:
#           ax1.plot(i, y, "ro" if signal == "BUY" else "go")
#
#     ax2 = ax1.twinx()
#     ax2.plot(range(len(interests)), interests, label="수익률", color="blue")
#     plt.show()
#
# def backtest(prices, initial_balance):
#     balance = initial_balance
#     quantity = 0
#     ma20 = []
#     ma60 = []
#     interests = []
#
#     for i in range(len(prices)):
#         ...
#     show_graph(prices, ma20, ma60, interests)
#
# sample_prices = load_prices("sample.json")
# backtest(sample_prices, 1000 * 10000)
#
# rfozus48v-image.png
#
# 코드잇에서는 [데이터 분석, 기초에서 실전까지] 로드맵에서 Matplotlib를 다루는 커리큘럼을 제공하고 있으니 한번 살펴보세요!
#
# 내 컴퓨터가 아니라 다른 곳에서 실행하기
# 우리가 만든 코드는 한계가 명확합니다. 데이터를 파이썬 변수로 내 컴퓨터에 저장하고요, 혹시 컴퓨터 전원이 꺼지거나 한다면 자동 매매 코드도 멈출 겁니다.
#
# 보통 이런 경우엔 내 컴퓨터에서 코드를 실행하는 게 아니라 마이크로소프트나 아마존같이 큰 회사에서 제공하는 클라우드 서비스에 코드를 올려놓고 실행하는데요.
#
# 이렇게 코드를 올려놓는 걸 프로그래밍 분야에선 코드를 "배포한다(Deploy)"라고 표현합니다.
#
# 여러 사람들과 협업하기
# 프로그래밍 분야의 진정한 장점은 수많은 사람들과 코드를 공유하면서 협업할 수 있다는 점입니다.
#
# 아까 살펴봤던 Pandas, Matplotlib은 사람들이 쉽게 가져다 쓸 수 있을 뿐만 아니라 어떻게 만들어진 것인지 소스 코드까지 공개되어 있는데요. 오늘날의 Pandas, Matplotlib 심지어 파이썬조차도 전 세계 수많은 개발자들이 다 같이 코드를 수정하면서 만들어진 것들입니다.
#
# 이런 공개된 코드를 모아 놓은 사이트인 깃허브에 들어가 보면 실제 코드를 확인해 볼 수 있어요. Python의 깃허브에는 수많은 개발자들이 함께 만들고 있는 코드를 볼 수 있죠.
#
# 최근엔 이런 협업을 할 때 Git이라는 도구를 사용하는데요. Git을 사용하면 인터넷으로 코드를 공유하고 여러 사람들과 함께 협업을 할 수 있어요.
#
# 그리고 내 컴퓨터가 아니라 다른 곳에 배포해서 코드를 실행할 때에도 Git으로 코드를 관리하는 게 필수인데요.
#
# 코드잇에서는 [Git으로 배우는 버전 관리] 로드맵에서 관련된 내용을 배워 볼 수 있어요.
#
# Django로 웹사이트 만들기
# 파이썬을 배우면 정말 다양한 일을 할 수 있어요. 이번에 만들어 본 주식 자동 매매뿐만 아니라, 페이스북이나 인스타그램, 틱톡 같은 웹서비스도 만들 수 있는데요. 특히 파이썬에서는 Django라는 게 있는데 이걸 사용하면 웹 사이트를 꽤 손쉽게 만들 수 있답니다.
#
# 주식에 관심이 있다면 주식과 관련된 웹 서비스를 만들어서 새로운 수익화를 해 보는 건 어떨까요?
#
# 나만의 웹사이트를 만들어 보고 싶으신 분들은 [Django 웹 개발]에 한 번 도전해 보세요.
#
# 이번 레슨에서는 이렇게 파이썬을 배우고 나서 더 배우면 좋을 내용에 대해 살펴봤습니다. 아주 간단하게나마 주식 자동 매매 코드를 만들어 봤지만, 앞으로 코딩을 계속 배우면서 이 코드를 업그레이드해 보는 것도 좋겠죠? 새롭게 시작할 여러분의 파이썬 공부를 응원하겠습니다.