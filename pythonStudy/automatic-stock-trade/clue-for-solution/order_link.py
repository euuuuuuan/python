# 이제 앞에서 만든 함수에 API 연동을 하면서 구체적으로 내용을 채워 보도록 하겠습니다.
#
# API 문서에서는 리퀘스트를 보낼 때 어떤 주소로 어떤 헤더와 쿼리 파라미터 그리고 바디를 채워서 보내 주면 되는지, 리스폰스로 오는 데이터는 어떤 형식인지 적혀 있었습니다. 실제로 코딩을 할 때는 API 문서를 항상 켜 두고, 정해진 형식에 맞게 리퀘스트를 보내는 코드를 작성하고, 테스트해 본 다음, 실제 코드에 적용하는 식으로 반복적인 작업을 한다고 생각하시면 됩니다.
#
# clear_orders() 함수
# API 문서를 보면 "주식일별주문체결조회"에서 내가 넣은 주문의 체결 여부를 확인할 수 있고요, "주식주문(정정취소)"에서 주문을 취소할 수 있을 거 같습니다.
#
# 예를 들어서 내 주문을 모두 조회해서 리스트로 리턴해 주는 함수 fetch_orders()라는 함수가 있다고 가정하고 주식을 취소하는 함수 cancel_order()라는 함수가 있다고 가정한다면, clear_orders() 함수를 어떻게 구현할지 대략적인 코드로 써 보면 이런 식일 겁니다.
#
#
# def clear_orders():
#     orders = fetch_orders()
#     for order in orders:
#         cancel_order(order)
# fetch_orders() 함수
# 그럼 먼저 fetch_orders()라는 함수랑 cancel_orders()라는 함수부터 구현해 볼까요?
#
# "주식일별주문체결조회" API 문서를 보면 다음과 같은 형식으로 리퀘스트를 보낼 수 있을 거 같습니다.
#
# 주소는 /uapi/domestic-stock/v1/trading/inquire-daily-ccld 이고요,
#
# GET이라는 메소드로 보냅니다.
#
# 헤더에는 아래와 같은 값들이 필요합니다.
#
#
# authorization: Bearer <access token 값>
# appkey: <appkey 값>
# appsecret: <appsecret 값>
# tr_id: VTTC8001R
# 쿼리 파라미터로는 아래와 같은 값이 필요합니다.
#
#
# CANO: <계좌번호 앞 8글자>
# ACNT_PRDT_CD: <계좌번호 뒤 2글자>
# INQR_STRT_DT: <조회 시작할 날짜>
# INQR_END_DT: <조회 끝낼 날짜>
# SLL_BUY_DVSN_CD: 00
# INQR_DVSN: 00
# PDNO: <종목 코드>
# CCLD_DVSN: 02 (미체결만 조회)
# ORD_GNO_BRNO: ""
# ODNO: ""
# INQR_DVSN_3: 00
# INQR_DVSN_1: ""
# CTX_AREA_FK100: ""
# CTX_AREA_NK100: ""
# 여기서 계좌 번호, 종목 코드는 바뀔 수도 있는 값이니까 함수의 파라미터로 받아 오면 좋을 거 같네요.
#
# 계좌 번호 앞 8글자, 계좌 번호 뒤 2글자는 전체 계좌 번호를 가지고 문자열 슬라이싱을 활용해서 잘라서 보내 주면 될 것 같습니다.
#
# 그리고 조회 시작할 날짜, 조회 끝낼 날짜 이 두 가지를 YYYYMMDD 형식으로 적어서 전달해 주어야 하는데요. 저는 오늘 날짜를 기준으로 조회할 겁니다.
#
# 혹시 파이썬 [datetime 모듈]에 대해서 잠깐 배웠던 내용을 기억하시는 분들도 있겠지만, 다시 그 내용을 찾아보면서 코드를 적어 보면 아래와 같은 코드로 오늘 날짜를 20240501 같은 형태로 만들 수 있습니다.
#
#
# from datetime import datetime
#
# today = datetime.today().strftime('%Y%m%d')
# 그리고 리스폰스로 오는 데이터에서는 output1이라는 속성에 주문에 대한 정보가 리스트로 담겨 있으니 이 값을 리턴하고, 만약 이 값을 가져오지 못한다면 빈 리스트를 리턴하면 될 거 같습니다.
#
# 이렇게 파악한 정보를 가지고 함수를 만들면 아래와 같습니다.
#
#
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
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         return data["output1"]
#     except Exception as e:
#         print(e)
#         return []
# 마찬가지로 cancel_order() 함수를 구현해 보겠습니다. "주식주문(정정취소)" API를 사용할 건데요.
#
# 이 API는 /uapi/domestic-stock/v1/trading/order-rvsecncl라는 주소로 POST 메소드를 써서 보내야 합니다.
#
# 여기서는 헤더와 바디로 데이터를 보내는데요. 바디에는 계좌 번호 정보와 정정 또는 취소할 주문 번호가 필요합니다. 그래서 이 두 가지를 account와 order_no라는 파라미터로 받기로 했습니다.
#
# 바디는 JSON 형식으로 보내야 하기 때문에, 파라미터로 넘겨주기 전에 json.dumps() 함수로 JSON 형식으로 변환해서 보내 주었습니다.
#
# 리턴 값으로는 리퀘스트가 성공했는지 여부를 True/False로 리턴할 건데요. API 문서를 보면 리스폰스 바디에 있는rt_cd라는 값이 문자열 0 이면 성공이라고 알려 주고 있습니다. 그래서 리턴 값으로 data["rt_cd"] == "0"라는 값을 리턴하기로 했어요. 문자열 값이라는 것에 주의하세요.
#
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
# 이렇게 만든 두 함수를 활용해서 clear_orders() 함수를 구현하면 다음과 같습니다. 계좌 번호와 종목 번호를 account, code라는 파라미터로 받아서 사용할 건데요. 우선 fetch_orders() 함수로 현재 미체결된 주문을 리스트로 가져와서, 이 주문들을 하나씩 for반복문을 사용해서 cancel_order() 함수로 취소해 줄 겁니다.
#
# 주문 번호는 fetch_orders()에서 가져온 값에서 odno라는 속성에 담겨 있습니다. 이건 fetch_orders() 함수를 만들 때 사용한 "주식일별주문체결조회" API의 문서에서 알게 된 것입니다.
#
#
# def clear_orders(account, code):
#     orders = fetch_orders(account, code)
#     for order in orders:
#         order_no = order["odno"]
#         result = cancel_order(account, order_no)
#         print(f"{order_no} 취소 성공" if result else f"{order_no} 취소 실패")
# fetch_avail() 함수
# 이번엔 현재 주문 가능한 수량을 조회하는 함수인 fetch_avail() 함수를 구현해 보겠습니다. "매수 가능 조회" API를 사용할 거예요.
#
# /uapi/domestic-stock/v1/trading/inquire-psbl-order라는 주소로 GET 메소드를 사용해서 리퀘스트를 보내면 되는 것 같습니다. 헤더 값이랑 쿼리 파라미터 값을 보내야 하는데, 여기서도 계좌 번호랑 종목 코드가 필요합니다. 그리고 주문 가능한 수량을 조회하기 위한 금액도 필요해요. account, code, target_price라는 파라미터를 받아 와서 사용하겠습니다.
#
# 우리는 우리가 정해 놓은 가격으로 주문 가능한 수량을 조회할 거기 때문에 지정가 조회를 할 겁니다.
#
# 여기서 한 가지 주의할 점이 있는데요. 한국투자증권의 API가 특이하게 금액을 문자열 타입으로 받기 때문에, target_price를 숫자형으로 보내면 안 되고 str()이라는 함수를 써서 문자열로 자료형을 바꿔 주어야 한다는 점입니다. 이런 걸 형 변환이라고 하는데, 혹시 잘 기억이 나지 않으시는 분들은 [형 변환 - 프로그래밍 핵심 개념 in Python]에서 관련된 내용을 찾아보세요.
#
# 리스폰스 바디에서 저는 "미수 없는 매수 가능 수량" 값만 쓸 겁니다. output 속성 안에서 또 nrcvb_buy_qty라는 값을 가져와서 쓸 거기 때문에 data["output"]["nrcvb_buy_qty"]라는 코드로 값을 리턴했습니다. 만약에 이 과정에서 실패가 발생한다면, 즉 원하는 데이터를 가져올 수 없다면 가능한 수량을 0이라고 리턴하고, 아무런 동작도 하지 않도록 만들 겁니다.
#
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
#         return int(data["output"]["nrcvb_buy_qty"])  # 미수 없는 매수 가능 수량
#     except Exception as e:
#         print(e)
#         return 0
# fetch_quantity() 함수
# 이번에는 매도 가능한 수량을 받아오는 함수를 만들겠습니다. "주식잔고조회" API를 사용할 건데요. 여기서는 예수금뿐만 아니라 내 계좌에 어떤 종목들을 보유하고 있는지도 조회할 수 있습니다.
#
# /uapi/domestic-stock/v1/trading/inquire-balance라는 주소로 GET 리퀘스트를 보내면 되고요, 헤더랑 쿼리 파라미터로 값을 보내야 하는데 여기서도 내 계좌 번호가 필요합니다. 그래서 파라미터로 account라는 값을 받을 겁니다. 그리고 code라는 파라미터로 종목 코드 값을 받을 건데요. 특정 종목을 얼마나 보유하고 있는지 찾아보고, 그 수량을 숫자로 리턴하는 함수를 만들어 볼 거예요.
#
# 리스폰스 바디에서 output1이라는 값이 있는데 이 값은 API 문서에서는 "Array"라고 표현되어 있죠. 파이썬에서는 리스트에 해당하는 값이라는 건데요. 이 리스트에 각 종목들에 대한 데이터가 들어가 있고, 그 데이터 안에서 보유 수량을 가져올 수 있는 식입니다.
#
# 그래서 for반복문을 통해서 data["output1"]에 있는 모든 종목 데이터를 돌면서, 특정 종목 코드랑 일치하는 요소를 찾아낸 다음에 거기서 보유 수량에 해당하는 hldg_qty 값을 리턴하는 식으로 구했습니다.
#
# 만약 for반복문을 모두 돌았는데도 리턴하지 않았다면 보유한 수량이 없다는 이야기이니까 0을 리턴하고, 이 과정에서 어떤 오류가 발생했다면 아무 동작도 하지 않기 위해서 0을 리턴했습니다.
#
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
#         "OFL_YN": "",  # 공란
#         "INQR_DVSN": "02",  # 종목별
#         "UNPR_DVSN": "01",  # 단가 구분 기본값
#         "FUND_STTL_ICLD_YN": "N",
#         "FNCG_AMT_AUTO_RDPT_YN": "N",
#         "PRCS_DVSN": "00",  # 전일 매매 포함
#         "CTX_AREA_FK100": "",
#         "CTX_AREA_NK100": ""
#     }
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         for item in data["output1"]:
#             if item["pdno"] == code:
#                 return int(item["hldg_qty"])
#         return 0
#     except Exception as e:
#         print(e)
#         return 0
# order() 함수
# 마지막으로 매수 또는 매도 주문을 넣는 함수를 구현해 볼게요. "주식주문(현금)" API를 쓸 건데요. 여기서는 특정 종목에 대해서 시장가가 아닌 지정가로 원하는 수량만큼 주문을 넣을 겁니다.
#
# API 문서를 보면 /uapi/domestic-stock/v1/trading/order-cash라는 주소로 POST 리퀘스트를 보냅니다. 리퀘스트 바디에 주문에 대한 정보를 담아서 보내면 주문이 제출되는 식인 거 같습니다.
#
# 리퀘스트 헤더에서는 tr_id라는 값에 따라 매수 또는 매도 주문을 다르게 할 수 있는 거 같은데요. 그래서 함수를 호출할 때도 매수 또는 매도를 원하는 대로 할 수 있게 "BUY" 또는 "SELL"이라는 값을 받는 order_type이라는 파라미터를 받기로 했습니다. 그리고 계좌 번호랑 종목 코드, 수량, 원하는 가격 데이터가 필요해서 각각 account, code, amount, target_price라는 파라미터로 값을 받았습니다.
#
# 이 API에서도 한 가지 주의할 점을 미리 알려 드리자면, 한국투자증권 API에서는 숫자형을 거의 사용하지 않고 문자열로 받기 때문에 ORD_QTY에 필요한 수량 값이나 ORD_UNPR 에 필요한 가격 값을 보낼 때 문자열로 형 변환을 해서 보내 줘야 합니다.
#
# 만든 리퀘스트 바디는 보내기 전에 JSON 형식으로 바꾸기 위해 json.dumps() 함수를 사용했습니다.
#
# 주문이 성공적으로 들어갔는지 여부는 리스폰스 바디에서 rt_cd 값이 문자열 "0"인지 확인하는 식으로 처리했어요.
#
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
#     try:
#         res = requests.post(url, headers=headers, json=body)
#         data = res.json()
#         return data["rt_cd"] == "0"
#     except Exception as e:
#         print(e)
#         return False
# API 함수 적용하기
# 이제 만든 함수를 적용해 볼게요. 앞에서 작성했던 while반복문에서 함수들을 호출했었는데요. 함수를 사용하는 방법이 조금씩 달라졌으니까, 그 부분을 수정해 보겠습니다.
#
# 계좌 번호랑 종목 코드에 해당하는 값을 맨 위에 ACCOUNT랑 CODE라는 변수에 저장해서 썼고요. 이걸 아래쪽의 while반복문에서 적용해 줬어요.
#
#  main.py
#
#
# from time import sleep
# import requests
# from datetime import datetime
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
# ACCOUNT = "..."
# CODE = "005930"
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
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
#         return data["rt_cd"] == "0"
#     except Exception as e:
#         print(e)
#         return False
#
# # 자동 매매 코드
#
# prices = []
# ma20 = []
# ma60 = []
#
# while True:
#     # 현재 가격 조회
#     current_price = fetch_current_price("005930")
#     if current_price is not None:
#         prices.append(current_price)
#         # 이동 평균선 계산
#         ma20.append(ma(prices, 20))
#         ma60.append(ma(prices, 60))
#         # 투자 전략 확인
#         signal = ma_signal(ma20, ma60)
#         print(
#             f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
#         # 과거 주문을 조회하고 미체결된 주문이 있으면 취소하기
#         clear_orders(ACCOUNT, CODE)
#
#         # 전략에 따라 주문하기
#         amount = 0
#         if signal == "BUY":
#             # 매수 주문 가능한 수량 조회하기
#             amount = fetch_avail(ACCOUNT, CODE, prices[-1])
#         elif signal == "SELL":
#             # 보유 수량 업데이트하기
#             amount = fetch_quantity(ACCOUNT, CODE)
#         if amount > 0:
#             result = order(signal, ACCOUNT, CODE, amount, prices[-1])
#             if result:
#                 print(f"{signal} {CODE} {amount}개 {prices[-1]}원 주문 성공")
#     sleep(60)
#
# 총 평가금 확인
# 마지막으로 한 가지만 더 추가해 볼게요. 자동 매매가 잘 이루어지고 있는지 체크하기 위해서 현재 내 잔고에 얼마가 있는지 1분마다 확인해 볼 거예요. 아까 만들었던 fetch_quantity() 함수를 조금 변형해서 만들 겁니다. "주식잔고조회" API를 보면 총 평가금액을 가져올 수 있는데요. 이걸 가지고 확인해 보겠습니다. 이번에는 output2라는 속성의 첫 번째 요소(0번 인덱스)에서 총 평가금액에 해당하는 tot_evlu_amt 값을 가져올 거예요.
#
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
#         "OFL_YN": "", # 공란
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
# 전체 코드
# 이렇게 작성해 본 전체 코드입니다. 간혹 API 리퀘스트를 너무 자주 보내면 오류가 나는데, 그런 경우에는 sleep() 함수를 활용해서 적절히 딜레이를 주면 됩니다. 예를 들어서 sleep(0.2)이라고 하면 0.2초 딜레이를 주겠다는 의미입니다.
#
#  main.py
#
#
# from time import sleep
# import requests
# from datetime import datetime
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
# ACCOUNT = "..."
# CODE = "005930"
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
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
#         return data["rt_cd"] == "0"
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
#         "OFL_YN": "", # 공란
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
#         return data["output2"][0]["tot_evlu_amt"]
#     except Exception as e:
#         print(e)
#         return None
#
# # 자동 매매 코드
#
# prices = []
# ma20 = []
# ma60 = []
#
# while True:
#     # 현재 가격 조회
#     current_price = fetch_current_price(CODE)
#     if current_price is not None:
#         prices.append(current_price)
#         # 이동 평균선 계산
#         ma20.append(ma(prices, 20))
#         ma60.append(ma(prices, 60))
#         # 투자 전략 확인
#         signal = ma_signal(ma20, ma60)
#         print(
#             f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
#         # 과거 주문을 조회하고 미체결된 주문이 있으면 취소하기
#         sleep(0.2)
#         clear_orders(ACCOUNT, CODE)
#
#         # 전략에 따라 주문하기
#         amount = 0
#         if signal == "BUY":
#             # 매수 주문 가능한 수량 조회하기
#             amount = fetch_avail(ACCOUNT, CODE, prices[-1])
#         elif signal == "SELL":
#             # 보유 수량 업데이트하기
#             amount = fetch_quantity(ACCOUNT, CODE)
#         if amount > 0:
#             sleep(0.2)
#             result = order(signal, ACCOUNT, CODE, amount, prices[-1])
#             if result:
#                 print(f"{signal} {CODE} {amount}개 {prices[-1]}원 주문 성공")
#     sleep(0.2)
#     eval = fetch_eval(ACCOUNT)
#     print(f"총 평가금: {eval}")
#     sleep(60)
#
# 실제 거래소에서 자동 매매를 하려면?
# API 문서에도 나와 있지만 실전에서는 API 리퀘스틀 보내는 주소가 다릅니다. 모의 투자에서 쓰던 URL 경로는 같지만 앞에서 변수로 지정했던 BASE_URL 을 바꿔 주어야 할 겁니다.
#
# order_link_1.png
#
# 그리고 또 한 가지 다른 게 있는데요. 예를 들면 주식주문(현금) API 문서를 보시면 리퀘스트로 보내는 값 중에서 거래 ID에 해당하는 tr_id 값이 다른 경우가 종종 있습니다. 이 부분도 잘 확인해 봐야겠죠?
#
# order_link_2.png