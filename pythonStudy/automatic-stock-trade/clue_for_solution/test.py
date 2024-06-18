# 이번 레슨에서는 test.py라는 파일을 임시로 만들고 이 파일에서 앞으로 쓸 코드들을 만들면서 테스트해 볼 거예요.
#
# 이동 평균선 구하기
# 가장 먼저 이동 평균선을 구하는 함수부터 구현해 보겠습니다. 앞에서 잠깐 살펴봤던 평균 구하는 법을 다시 살펴보자면, 파이썬의 sum() 함수를 활용해서 평균을 구했었죠.
#
#
# data = [1, 4, 3, 5, 1]
# avg = sum(data) / 5
# 이걸 가지고 values라는 리스트를 파라미터로 받아서 최근 20개의 이동 평균값을 리턴하는  ma20()라는 함수를 구현해 볼게요. indicator.py라는 파이썬 파일을 만들고 함수를 구현하겠습니다.
#
# 일단 values 리스트에서 최근 20개의 요소만 리스트 슬라이싱으로 잘라 내고 (values[-20:]) 이 리스트의 평균을 구하면 됩니다.
#
#  test.py
#
#
# def ma20(values):
#     if len(values) >= 20:
#         target_values = values[-20:]
#         return sum(target_values) / 20
#     else:
#         return None
# 코드를 보니까 20이라는 숫자가 반복되는 거 보이시나요? 이걸 변수로 만들면 재활용할 수 있을 거 같습니다. 20이라는 고정된 숫자 대신에 함수에서 파라미터로 window_size라는 값을 받아서 쓰도록 고쳐 볼게요. (참고로 값을 계산할 때 20개의 범위가 계속 이동하잖아요? 보통 프로그래밍에선 이렇게 이동하는 범위를 window라고 표현합니다.)
#
#  test.py
#
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
# 이 함수가 잘 동작하는지 한번 테스트해 볼게요. 0부터 19까지 담겨 있는 리스트에서 MA5와 MA10을 구해 볼게요.
#
#  test.py
#
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
#
# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# ma5 = []
# ma10 = []
#
# for i in range(len(data)):
#     ma5.append(ma(data[:i + 1], 5))
#     ma10.append(ma(data[:i + 1], 10))
# print(ma5)
# print(ma10)
#
#
# [None, None, None, None, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0]
# [None, None, None, None, None, None, None, None, None, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5]
# 투자 전략 구현하기
# 이동 평균선 투자 전략을 구현해 봅시다. 앞에서 투자 전략을 살펴보면서 만들었던 코드 기억나시나요? MA20과 MA60 값이 담겨 있는 리스트가 있을 때, 현재 시점의 값과 이전 시점의 값을 비교해서 골든 크로스인 경우 매수 신호, 데드 크로스인 경우 매도 신호로 판단하기로 했었습니다.
#
#
# prices = []
# ma20 = []
# ma60 = []
#
# # i는 현재 시점을 가리키는 인덱스라고 가정
# prev = ma20[i-1] - ma60[i-1]
# current = ma20[i] - ma60[i]
#
# if prev < 0 and current >= 0:
#     # 매수 신호
# elif prev >= 0 and current < 0:
#     # 매도 신호
# 이 코드를 응용해서 짧은 이동 평균선 리스트 ma_short_term 그리고 긴 이동 평균선 리스트 ma_long_term을 파라미터로 받고, 가장 마지막 값(-1번 인덱스 값)과 그 이전의 값(-2번 인덱스 값)을 비교하는 함수를 만들게요. 매수 신호이면 "BUY" 매도 신호이면 "SELL"을 리턴하고, 그 외의 경우엔 None을 리턴하는 함수를 구현해 보았습니다.
#
#  test.py
#
#
# def ma(values, window_size):
#     if len(values) >= window_size:
#         target_values = values[-window_size:]
#         return sum(target_values) / window_size
#     else:
#         return None
#
# def ma_signal(ma_short_term, ma_long_term):
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
# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# ma5 = []
# ma10 = []
#
# for i in range(len(data)):
#     ma5.append(ma(data[:i + 1], 5))
#     ma10.append(ma(data[:i + 1], 10))
# print(ma5)
# print(ma10)
#
# 그런데 ma_short_term과 ma_long_term 리스트 값에 따라서 이 계산을 할 수 없는 경우가 있어요. 위에 이동 평균선을 구하는 함수를 테스트했을 때 None 값이 리스트에 들어가는 경우가 있었잖아요? 이런 경우엔 빼기 연산을 할 수가 없습니다.
#
# 그리고 리스트에 요소가 하나도 없거나 1개인 경우에는 이전 값([-1])이나 그 이전의 값([-2])이 존재하지도 않고요. 그래서 오류가 나지 않도록 아래처럼 예외적인 경우에는 None을 리턴하는 코드도 추가해 주겠습니다.
#
#  test.py
#
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
# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# ma5 = []
# ma10 = []
#
# for i in range(len(data)):
#     ma5.append(ma(data[:i + 1], 5))
#     ma10.append(ma(data[:i + 1], 10))
# print(ma5)
# print(ma10)
#
# 아까 전에 ma() 함수를 테스트했던 코드는 이제 지워 줄게요.
#
#  test.py
#
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
# 테스트해 보기
# 이번에는 테스트용 JSON 파일에서 가격 데이터를 가져와서 앞에서 만든 함수들을 테스트해 볼게요. 요구 사항에 있었던 sample.json 파일을 다운로드하여서 프로젝트 폴더에 둡시다.
#
# json.load() 함수를 사용해서 가격 데이터만 불러오는 load_prices() 함수를 먼저 작성해 볼게요.
#
# 테스트용 JSON 파일을 불러오면 사전이 하나의 요소로 담겨 있는 리스트 형태입니다. 각 요소에는 일분봉 데이터가 들어가 있는데요. 현재 가격을 가져오려면 stck_prpr 속성을 참조하면 됩니다.
#
#  test.py
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
#
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
# sample_prices = load_prices("sample.json")
# print(sample_prices)
#
# [17470, 17350, 17510, 17670, 17330, ...]
# 이제 이 sample_prices 리스트를 가지고 만들어 놓은 ma() 함수랑 ma_signal() 함수를 테스트해 볼게요.
#
#  test.py
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
# def test(prices):
#     ma20 = []
#     ma60 = []
#     for i in range(len(prices)):
#         ma20.append(ma(prices[:i], 20))
#         ma60.append(ma(prices[:i], 60))
#         signal = ma_signal(ma20, ma60)
#         print(f"시그널: {signal} MA20: {ma20[-1]} MA60: {ma60[-1]}")
#
# sample_prices = load_prices("sample.json")
# test(sample_prices)
#
# 출력 결과를 살펴보면 MA20 값이 MA60보다 작았다가 커지는 순간 BUY 시그널이 잘 나오는 걸 확인할 수 있고요, 반대로 MA20 값이 컸다가 작아지는 순간 SELL 시그널이 잘 나오는 걸 확인할 수 있네요.
#
#
# ...
# 시그널: None MA20: 18217.0 MA60: 18233.666666666668
# 시그널: None MA20: 18222.0 MA60: 18224.0
# 시그널: BUY  MA20: 18226.5 MA60: 18214.333333333332
# 시그널: None MA20: 18230.5 MA60: 18205.166666666668
# 시그널: None MA20: 18220.5 MA60: 18205.0
# 시그널: None MA20: 18211.0 MA60: 18205.833333333332
# 시그널: SELL MA20: 18200.0 MA60: 18207.0
# 시그널: None MA20: 18193.5 MA60: 18209.666666666668
# 시그널: None MA20: 18178.5 MA60: 18209.0
# ...