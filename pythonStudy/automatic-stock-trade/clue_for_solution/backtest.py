# 앞에서 작성한 test.py 파일과 test() 함수를 수정해서 백테스트를 해 보겠습니다.
#
# 우선 파일 이름을 backtest.py로 바꿉시다.
#
# 백테스트를 하려면 잔고 금액이 있어야 하고요, 이 금액을 가지고 BUY 시그널이 오면 주식을 전량 매수했다가 SELL 시그널이 오면 전량 매도하는 식으로 코드를 짜 보겠습니다. 주식을 샀다가 파는 걸 흉내 내려면 현재 보유 수량도 저장해야겠죠?
#
# backtest()라는 이름으로 함수 이름을 바꾸고, 파라미터로는 가격 데이터가 담겨 있는 prices 리스트, 그리고 초기 잔고 금액인 initial_balance라는 파라미터를 받도록 하겠습니다.
#
# 함수 안에서 잔고와 수량에 해당하는 balance와 quantity라는 변수를 만들고요, 각 시그널마다 이 값을 변경하면서 매수와 매도를 흉내 내겠습니다.
#
#  backtest.py
#
#
# import json
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
# def backtest(prices, initial_balance):
#     balance = initial_balance
#     quantity = 0
#     ma20 = []
#     ma60 = []
#
#     for i in range(len(prices)):
#         ma20.append(ma(prices[:i], 20))
#         ma60.append(ma(prices[:i], 60))
#         signal = ma_signal(ma20, ma60)
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
# sample_prices = load_prices("sample.json")
#
# 각 시점에 시그널이랑 수익률 변화가 어떤지 체크하기 위해서 출력을 해 볼게요. 수익률은 대략 다음과 같은 식으로 계산해 볼 수 있을 겁니다.
#
#
# 현재 자산 가치 = 잔고 + 현재 가격 * 보유 수량
# 순이익 = 현재 자산가치 - 초기 잔고
# 수익률(%) = 순이익 / 초기 잔고 * 100
# 이걸 파이썬 코드로 구현해 보면 아래와 같습니다.
#
#
# asset = balance + prices[i] * quantity
# interest = asset - initial_balance
# roi = interest / initial_balance * 100
# 이 코드는 조금 더 짧게 아래처럼 줄일 수도 있어요.
#
#
# roi = ((balance + prices[i] * quantity) / initial_balance - 1) * 100
# 이걸 백테스트 함수에 적용시켜서 출력하는 코드까지 써 보면 아래와 같습니다. 초기 잔고 금액을 1,000만 원으로 설정하고 한 번 실행해 볼게요.
#
#  backtest.py
#
#
# import json
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
# def backtest(prices, initial_balance):
#     balance = initial_balance
#     quantity = 0
#     ma20 = []
#     ma60 = []
#
#     for i in range(len(prices)):
#         ma20.append(ma(prices[:i], 20))
#         ma60.append(ma(prices[:i], 60))
#         signal = ma_signal(ma20, ma60)
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
#
# 시그널: SELL 수익률: 0.0%
# 시그널: BUY 수익률: 0.0%
# 시그널: SELL 수익률: -0.5510000000000015%
# 시그널: BUY 수익률: -0.5510000000000015%
# 시그널: SELL 수익률: -0.27000000000000357%
# 시그널: BUY 수익률: -0.27000000000000357%
# 시그널: SELL 수익률: -0.4361999999999977%
# 수익률이 썩 좋은 것 같지는 않지만 그럭저럭 동작은 하는 것 같네요. 실제 주식 자동 매매를 하려면 다양한 데이터로 충분히 테스트해 보면서 수익률을 검토해야 할 거 같습니다.