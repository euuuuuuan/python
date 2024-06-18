# 앞에서 이동 평균선 구하는 함수, 투자 전략 함수, 그리고 주식 현재가를 받아 오는 함수를 만들어 봤습니다. 이번 레슨에서는 이것들을 합쳐서, 실시간으로 일분마다 주식 현재가를 받아 오면서 이동 평균선을 계산하고, 투자 전략을 판단하는 코드를 만들어 보겠습니다.
#
# main.py 라는 파일을 만들고 구현할 거예요. 그리고 필요한 함수들은 아까 backtest.py에서 구현했던 걸 그대로 가져와서 쓸 겁니다.
#
# 1분마다 코드 실행하기
# 프로젝트 요구 사항에 제시된 것처럼, while문과 sleep() 함수를 활용해서 만들어 볼 건데요. 일단 main.py라는 파일을 만들고 여기에 큰 틀만 짜 보겠습니다. time 모듈에서 sleep() 함수를 불러와서 while 루프를 만들었습니다.
#
#  main.py
#
#
# from time import sleep
#
# while True:
#     # 1분마다 할 동작
#     sleep(60)
# 1분마다 할 동작을 코멘트로 좀 더 구체적으로 적어 보면 이렇습니다.
#
#  main.py
#
#
# from time import sleep
#
# while True:
#     # 현재 가격 조회
#     # 이동 평균선 계산
#     # 투자 전략 확인
#     # 계좌 상태 확인하기
#     # 전략에 따라 주문하기
#     sleep(60)
# 앞에서 만든 함수 적용하기
# 이제 앞에서 만들어 두었던 함수를 적용해 봅시다. 이동 평균을 계산하는 ma() 함수, 투자 전략을 판단하는 ma_signal() 함수 그리고 주식 현재 가격을 받아 오는 fetch_current_price() 함수를 추가해 줬습니다. 그리고 while문 안에서 사용할 변수들을 정의할 건데요. 과거 데이터를 가져와서 테스트할 때처럼 현재 가격을 리스트로 모아 놓고, 이걸로 이동 평균값을 계산해야겠죠? 그래서 prices, ma20, ma60이라는 리스트 변수를 정의했습니다.
#
# 그리고 자동 매매를 할 주식의 종목 코드를 정해 놓고 쓰려고 CODE라는 변수에 저장했습니다.
#
#  main.py
#
#
# from time import sleep
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
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
# # 자동 매매 코드
#
# prices = []
# ma20 = []
# ma60 = []
#
# while True:
#     # 현재 가격 조회
#     # 이동 평균선 계산
#     # 투자 전략 확인
#     # 계좌 상태 확인하기
#     # 전략에 따라 주문하기
#     sleep(60)
#
# 이제 while문 안에서 각 함수를 실행해 볼게요. 현재 가격을 조회하고, 이동 평균선을 계산한 다음에 리스트에 값을 채우고, 투자 전략을 확인해 보죠.  일단 먼저 현재 가격을 받아 온  다음 이걸 prices 리스트에 쌓는 코드를 작성할게요. 혹시 현재가를 받아 오는 데 실패하는 경우가 있을 수도 있으니까, 받아 온 값이 None이 아닌 경우에만 쌓도록 하겠습니다.
#
#  main.py
#
#
# from time import sleep
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
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
#         # 투자 전략 확인
#         # 계좌 상태 확인하기
#         # 전략에 따라 주문하기
#     sleep(60)
#
# 그러고 나서 이동 평균선을 계산해 볼게요. ma() 함수를 사용해서 쌓아 주면 됩니다. 이걸로 ma_signal()을 구하고 출력해 보겠습니다.
#
#  main.py
#
#
# from time import sleep
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
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
#         print(f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
#         # 계좌 상태 확인하기
#         # 전략에 따라 주문하기
#     sleep(60)
#
# 참고로 이 코드는 현재가를 1분마다 받아 오는 코드이기 때문에, 주식 정규장이 열려 있을 때만 제대로 동작할 거예요.
#
# 필요한 함수 미리 만들어 두기
# 실제 API를 연동하기 전에 필요한 함수를 미리 만들어 두겠습니다. 이번 레슨에 있는 코드가 꼭 정답은 아니고 다양한 방식으로 코드를 만들 수 있을 거예요. 어떤 식으로 생각을 전개해 나가고 코드를 작성하는지 참고한다고 생각하시고 내용을 따라오시면 좋을 것 같습니다.
#
# 일단 API를 사용해서 어떤 동작을 할 수 있는지 한국투자증권 API 문서를 살펴보면 아래와 같은 내용을 찾을 수 있어요.
#
# 주식주문(현금): 매수 주문이나 매도 주문을 넣을 수 있음.
# 주식주문(정정취소): 주문 취소를 할 수 있음.
# 주식일별주문체결조회: 내가 넣은 주문의 체결 여부를 확인할 수 있음.
# 주식잔고조회: 내가 보유한 주식의 수량를 조회할 수 있음.
# 매수 가능 조회: 특정 종목에 대해서 내가 주문 가능한 금액과, 수량을 알 수 있음
# 앞에서 백테스트를 할 때는 잔고랑 보유 수량을 변수 하나에 저장해 놓고 썼었죠? 하지만 실제 주식 시장에서는 주문을 넣는다고 무조건 곧바로 구입하거나 판매할 수 있는 건 아닙니다. 매수 주문을 넣더라도 체결되지 않고 계속 기다리는 경우도 있거든요. 그래서 실제로 자동 매매를 제대로 구현하려면 꽤 복잡하게 코드를 작성해야 합니다.
#
# 여기서는 단순하게 코드를 작성해 볼게요. 1분마다 반복되는 코드를 실행할 건데, 주식 주문이 체결되었는지 추적하려면 코드가 복잡해지니까, 1분마다 미체결된 주문은 항상 전부 취소하고, 무조건 주문이 가능하면 주문을 넣는 식으로 진행해 보죠.
#
# 이걸 코멘트로 적어 보면 다음과 같습니다.
#
#  main.py
#
#
# from time import sleep
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
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
#         print(f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
#           # 과거 주문을 조회하고 미체결된 주문이 있으면 취소하기
#           # 매수 주문 가능한 수량 조회하기
#           # 보유 수량 업데이트하기
#         # 전략에 따라 주문하기
#     sleep(60)
#
# 이렇게 적어 놓은 코멘트에 해당하는 작업을 수행하는 함수를 빈 껍데기만 미리 만들어 보겠습니다.
#
# clear_orders()
# 현재 미체결인 주문을 모두 조회하고, 전부 취소하는 함수
# fetch_avail()
# 매수 가능한 수량을 받아 오는 함수
# fetch_quantity()
# 매도 가능한 수량을 받아 오는 함수
# order()
# 매수 또는 매도 주문을 하는 함수
# 참고로 이 해설에서는 완성된 코드를 가지고 설명하고 있기 때문에 코드가 꽤 잘 정리된 형태예요. 하지만 이 코드를 작성하기까지 여러 가지 시행착오가 있었습니다. 여러분도 실제로 직접 코딩할 때는 여러 시행착오를 겪으면서 형태를 수정하게 될 겁니다.
#
# 그래도 시행착오를 훨씬 줄이는 방법은 있을 거예요. 양이 많고 복잡한 코드를 작성할 때는 막막할 수 있잖아요? 그럴 땐 처음부터 자세한 것들을 모두 다루기 보다는 이런 식으로 큼지막한 작업들로 미리 나눠서 생각해 보시는 걸 추천드립니다. 일단 저런 함수가 다 완성되어 있다고 상상하는 거죠. 그리고 나눠 놓은 부분을 채워 넣으면서 조금씩 수정해 나가면 조금 수월하실 겁니다.
#
# 자, 그럼 이렇게 틀만 만들어 놓은 함수를 가지고 코드만 미리 작성해 보겠습니다. 다음 레슨에서는 이걸 바탕으로 실제 API 문서를 보면서 세부적인 내용을 채워 보도록 할게요.
#
#  main.py
#
#
# from time import sleep
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
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
# def clear_orders():
#     return
#
# def fetch_avail():
#     return 0
#
# def fetch_quantity():
#     return 0
#
# def order():
#     return
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
#         clear_orders()
#
#         # 전략에 따라 주문하기
#         amount = 0
#         if signal == "BUY":
#             # 매수 주문 가능한 수량 조회하기
#             amount = fetch_avail()
#         elif signal == "SELL":
#             # 보유 수량 업데이트하기
#             amount = fetch_quantity()
#         if amount > 0:
#             order()
#     sleep(60)