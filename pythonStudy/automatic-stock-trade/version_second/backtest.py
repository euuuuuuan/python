import json
import indicator
import strategy

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

def backtest(prices, initial_balance):
    balance = initial_balance
    quantity = 0
    ma20 = []
    ma60 = []

    for i in range(len(prices)):
        ma20.append(indicator.ma(prices[:i], 20))
        ma60.append(indicator.ma(prices[:i], 60))
        signal = strategy.ma_signal(ma20, ma60)

        if signal == "BUY":
            amount = balance // prices[i]  # 전량 매수
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

