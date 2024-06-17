# backtest 백테스트
import json


def calculate_moving_average(prices, window_size):
    moving_averages = []
    for i in range(window_size, len(prices) + 1):
        avg = sum(prices[i - window_size:i]) / window_size
        moving_averages.append(avg)
    return moving_averages


def generate_signals(ma20, ma60):
    signals = []
    for i in range(1, len(ma20)):
        if ma20[i - 1] < ma60[i - 1] and ma20[i] >= ma60[i]:
            signals.append("Buy")
        elif ma20[i - 1] >= ma60[i - 1] and ma20[i] < ma60[i]:
            signals.append("Sell")
        else:
            signals.append("Hold")
    return signals


# JSON 파일 불러오기 예제
def load_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


# 예제: sample.json 파일을 불러와서 이동 평균선과 매매 신호 계산
if __name__ == "__main__":
    data = load_json("sample.json")
    prices = [item['price'] for item in data['prices']]
    ma20 = calculate_moving_average(prices, 20)
    ma60 = calculate_moving_average(prices, 60)
    signals = generate_signals(ma20, ma60)
    print(signals)
