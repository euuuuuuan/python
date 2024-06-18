from time import sleep
import indicator
import strategy
import api

CODE = "005930"

# 자동 매매 코드

prices = []
ma20 = []
ma60 = []

while True:
    # 현재 가격 조회
    current_price = api.fetch_current_price("005930")
    if current_price is not None:
        prices.append(current_price)
        # 이동 평균선 계산
        ma20.append(indicator.ma(prices, 20))
        ma60.append(indicator.ma(prices, 60))
        # 투자 전략 확인
        signal = strategy.ma_signal(ma20, ma60)
        print(
            f"가격: {prices[-1]} MA20: {ma20[-1]} MA60: {ma60[-1]} 시그널: {signal}")
        # 과거 주문을 조회하고 미체결된 주문이 있으면 취소하기
        api.clear_orders(api.ACCOUNT, CODE)

        # 전략에 따라 주문하기
        amount = 0
        if signal == "BUY":
            # 매수 주문 가능한 수량 조회하기
            amount = api.fetch_avail(api.ACCOUNT, CODE, prices[-1])
        elif signal == "SELL":
            # 보유 수량 업데이트하기
            amount = api.fetch_quantity(api.ACCOUNT, CODE)
        if amount > 0:
            result = api.order(signal, api.ACCOUNT, CODE, amount, prices[-1])
            if result:
                print(f"{signal} {CODE} {amount}개 {prices[-1]}원 주문 성공")
    eval = api.fetch_eval(api.ACCOUNT)
    print(f"총 평가금: {eval}")
    sleep(60)

