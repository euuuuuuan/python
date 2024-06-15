# 주식 자동 매매 백테스트를 구현해 주세요.
# 주어진 sample.json 파일을 불러와서 백테스트를 진행해 주세요.
# JSON 데이터는 json 모듈의 json.load() 함수로 변환해 사용해 주세요. (자세한 설명은 아래에 있습니다.)
# 백테스트 단계마다 매매 신호와 수익률을 출력해 주세요.

# with open("파일 경로", "r") as f:
#     for line in f:
#         print(line)

# json.load() 함수로
# JSON 데이터를 파이썬 사전으로 변환해서 사용할 수 있어요
# import json
#
# data = None
# with open("sample.json", "r") as f:
#     data = json.load(f)
# print(data)

# 1. 백테스트
# 먼저 이동 평균선을 계산하는 함수를 만들어 봅시다.
#
# 이동 평균선을 가지고 매매 신호를 판단하는 함수를 만들어 보세요.
#
# JSON 파일을 불러옵니다.


# 주어진 데이터에서 현재가만 가져와서 이동 평균선을 계산합니다.
#
# 이동 평균선 매매 전략을 실행합니다.
#
# 잔고 금액을 설정하고,
# 전략에 따라 매매를 진행하면서 각 단계의 수익률을 계산합니다.

# 2. 자동 매매 구현하기
# # 우선 API로 현재 가격을 가져오는 함수를 작성해 보세요.
# #
# # while 반복문과 time 모듈의 sleep() 함수를 사용해서 1분마다 반복하는 코드를 작성합니다.
#
#
# from time import sleep
#
# while True:
#     # 1분마다 실행할 코드
#     sleep(60)
# 백테스트를 하면서 만들었던 함수들을 가져와서 자동 매매에 적용해 봅니다.
#
# 실제 API 리퀘스트를 보내는 함수를 작성해 보고, 이 함수를 while 반복문에 반영해 봅니다.


# 나의 문제 해결
import json

data = None
balance = 10000000
count = 0
# 함수 : 이동 평균선 값 계산
def calculate_moving_average(data, window_size):
    moving_averages = []
    for i in range(window_size, len(data)):
        avg = sum(data[i - window_size:i]) / window_size
        moving_averages.append(avg)
    return moving_averages

# 함수 : 매매 신호 생성
def generate_signals(ma20, ma60):
    signals = []
    for i in range(1, len()):
        if ma20[i - 1] < ma60[i - 1] and ma20[i] >= ma60[i]:
            signals.append("Buy")
        elif ma20[i - 1] >= ma60[i - 1] and ma20[i] < ma60[i]:
            signals.append("Sell")
        else:
            signals.append("Hold")
        return signals



# 이 변수는 나중에 JSON 파일에서 읽어온 데이터를 저장할 용도로 사용됩니다.
with open("sample.json", "r") as f:
    # 파일을 읽기 모드("r")로 열고 파일 핸들을
    # f라는 이름의 변수에 할당합니다. with 구문을 사용하면
    # 파일을 열고 닫는 과정을 자동으로 처리할 수 있습니다.
    data = json.load(f)
    # 파일 핸들 f에서 JSON 데이터를 읽어와
    # 파이썬 객체로 변환합니다.
    # 이렇게 하면 JSON 형식의 데이터가 파이썬에서
    # 사용할 수 있는 딕셔너리나 리스트와 같은 객체로 변환됩니다.

print(f"data 출력결과 : {data}")

ma20 = calculate_moving_average(data, 20)
print(f"ma20 출력결과 : {ma20}")

ma60 = calculate_moving_average(data, 60)
print(f"ma60 출력결과 : {ma60}")

signals = generate_signals(ma20, ma60)
print(f"signals 출력결과 : {signals}")



# # 각 단계에서의 매매 신호(`signals`)에 따라 매매를 수행하고 수익률을 계산합니다.
# for i in range(len(signals)):
#     if signals[i] == "Buy":
#         # 매수 로직을 여기에 구현합니다.
#         # 예를 들어, 현재 잔고를 이용하여 주식을 매수하고 잔고를 갱신하는 코드를 작성합니다.
#         current_price = data[60 + i]  # 예시로 매수 가격을 60일 이후의 데이터로 설정합니다.
#         shares_to_buy = balance // current_price  # 잔고를 이용하여 최대한 많은 주식을 매수합니다.
#         cost = current_price * shares_to_buy  # 매수에 소요된 금액 계산
#         balance -= cost  # 잔고 갱신
#
#         print(f"Step {i+1}: Bought {shares_to_buy} shares at {current_price:.2f}, Balance: {balance:.2f}")
#
#     elif signals[i] == "Sell":
#         # 매도 로직을 여기에 구현합니다.
#         # 예를 들어, 보유한 주식을 매도하고 그에 따른 잔고를 갱신하는 코드를 작성합니다.
#         current_price = data[60 + i]  # 예시로 매도 가격을 60일 이후의 데이터로 설정합니다.
#         shares_to_sell = 100  # 예시로 100주를 매도합니다.
#         income = current_price * shares_to_sell  # 매도로 인한 수익 계산
#         balance += income  # 잔고 갱신
#
#         print(f"Step {i+1}: Sold {shares_to_sell} shares at {current_price:.2f}, Balance: {balance:.2f}")
#
#     else:
#         # Hold일 경우 아무 작업도 수행하지 않습니다.
#         print(f"Step {i+1}: Hold, Balance: {balance:.2f}")
#
#     # 각 단계에서의 수익률 계산
#     profit = (balance - 10000000) / 10000000 * 100  # 초기 잔고 대비 수익률 계산
#     print(f"Step {i+1}: Profit {profit:.2f}%")
#
#     # 다음 단계를 위해 잔고 갱신
#     # 실제 시스템에서는 주식 거래와 잔고 관리가 필요합니다.