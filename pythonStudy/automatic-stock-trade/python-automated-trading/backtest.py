import json


def load_prices(filename):
    data = {}
    result = []

    with open(filename, "r") as f:
        data = json.load(f)
        f.close()
    for item in data:
        current_price = int(item["stck_prpr"])
        result.append(current_price)

    return result


def ma(values, window_size):
    if len(values) >= window_size:
        target_values = values[-window_size:]
        return sum(target_values) / window_size
    else:
        return None


def ma_signal(ma_short_term, ma_long_term):
    if len(ma_short_term) < 2 or len(ma_long_term) < 2:
        return None
    if None in ma_short_term[-2:] or None in ma_long_term[-2:]:
        return None
    prev = ma_short_term[-2] - ma_long_term[-2]
    current = ma_short_term[-1] - ma_long_term[-1]

    if prev < 0 and current >= 0:
        return "BUY"
    elif prev >= 0 and current < 0:
        return "SELL"
    else:
        return None


def backtest(prices, initial_balance):
    balance = initial_balance  # 잔고
    quantity = 0  # 수량
    ma20 = []
    ma60 = []

    for i in range(len(prices)):
        ma20.append(ma(prices[:i], 20))
        ma60.append(ma(prices[:i], 60))
        signal = ma_signal(ma20, ma60)

        if signal == "BUY":
            amount = balance // prices[i]  # 전량매수
            quantity += amount
            balance -= amount * prices[i]
        elif signal == "SELL":
            amount = quantity  # 전량 매도
            quantity -= amount
            balance += amount * prices[i]

        # 현재 수익률(%)
        roi = ((balance + prices[i] * quantity) / initial_balance - 1) * 100
        if signal is not None:
            print(f"시그널: {signal} 수익률: {roi}%")


sample_prices = load_prices("sample.json")
backtest(sample_prices, 1000 * 10000)