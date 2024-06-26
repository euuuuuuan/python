# 이번 레슨에서는 토픽에서 만들 자동 매매 프로그램의 투자 전략을 간단하게 살펴볼게요.
#
# 이동 평균선
# ghrluoqva-image.png
#
# 혹시 이동 평균선이라는 말 들어보신 적 있나요? "평균"이라는 단어에서 알 수 있듯이 이동하는 주식 가격의 평균으로 값을 만들고, 이걸 그래프로 그린 건데요.
#
# 위 이미지는 트레이딩 뷰라는 서비스에서 삼성전자 차트와 SMA20, SMA60 그래프를 그린 것입니다. 우리가 사용해 볼 것은 정확하게는 Simple Moving Average(줄여서 SMA) 한국말로는 단순 이동 평균이라는 값입니다.
#
# 이동 평균선은 평균을 낼 값의 개수를 정해야 하는데요. 예를 들어서 SMA20은 이전 20개의 값을 평균 낸 값을 모아서 그래프로 그린 것이고요, SMA60은 이전 60개의 값을 평균 낸 값을 그래프로 그린 겁니다. 위 이미지에서 파란색 선은 SMA20, 보라색 선은 SMA60입니다. 평균 구간을 길게 잡을수록(예를 들면 위 그래프에서 SMA60) 전반적인 추세를 알 수 있고요, 평균 구간이 짧을수록(예를 들면 위 그래프에서 SMA20) 주가 그래프에 가까워진답니다. SMA라고 줄여서 적기도 하지만 이번 토픽에서는 간단하게 MA20, MA60 이런 식으로 표현할게요.
#
# 이동 평균선 계산하기
# MA20의 값을 수식으로 표현하면 다음과 같아요.
#
#
# 현재 MA20 값 = (이전의 20개 값의 합) / 20
# 파이썬에서는 리스트 요소의 합을 구할 때 내장 함수인 sum()을 활용할 수 있어요. 예를 들어 숫자로 이루어진 data 리스트에서 모든 요소를 더한 값의 평균은 아래와 같이 구할 수 있습니다.
#
#
# data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 10, 15]
# avg = sum(data) / len(data)
# 만약에 이 데이터를 가지고 MA5를 만든다면 어떻게 만들 수 있을까요? data 리스트를 5개씩 나눠서, 평균값을 리스트에 모으면 될 겁니다.
#
#
# data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 10, 15]
# ma05 = []
# for i in range(5, len(data)):
#     avg = sum(data[i-5:i]) / 5
#     ma05.append(avg)
# print(ma05)
# 평균을 구하려면 최소한 이전에 다섯 개의 값이 필요하기 때문에 i의 값이 5에서부터 끝까지 바뀌도록 for 반복문을 만들었고요. 리스트 슬라이싱을 통해서 data[i-5:i] 같은 식으로 리스트를 다섯 개의 요소를 갖는 부분으로 자른 다음, 이 리스트로 평균을 냈어요.
#
# 구간 데이터의 합: sum(data[i-5:i])
#
# sum(data[i-5:i])는 선택된 구간 데이터의 합을 구합니다.
# 예를 들어, data가 [10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 10, 15]이고, i가 5라면, data[i-5:i]는 [10, 15, 20, 25, 30]입니다.
# sum([10, 15, 20, 25, 30])는 10 + 15 + 20 + 25 + 30 = 100입니다.
# 예시로 이해하기
# 첫 번째 반복 (i=5):
# 슬라이싱 구문: data[i-5:i] → data[5-5:5] → data[0:5]
# 추출된 데이터: [10, 15, 20, 25, 30]
# 평균 계산: (10 + 15 + 20 + 25 + 30) / 5 = 20
# ma05 리스트에 추가: [20]
# 두 번째 반복 (i=6):
# 슬라이싱 구문: data[i-5:i] → data[6-5:6] → data[1:6]
# 추출된 데이터: [15, 20, 25, 30, 35]
# 평균 계산: (15 + 20 + 25 + 30 + 35) / 5 = 25
# ma05 리스트에 추가: [20, 25]
# 세 번째 반복 (i=7):
# 슬라이싱 구문: data[i-5:i] → data[7-5:7] → data[2:7]
# 추출된 데이터: [20, 25, 30, 35, 40]
# 평균 계산: (20 + 25 + 30 + 35 + 40) / 5 = 30
# ma05 리스트에 추가: [20, 25, 30]
# 요약
# i가 5부터 시작하는 이유는 처음 5개의 요소를 평균 계산에 사용하기 위해서입니다.
# data[i-5:i]는 i에서 5를 뺀 인덱스부터 i까지의 요소를 슬라이싱합니다.
# 이는 5개 요소의 이동 평균을 계산하는데 필요한 구간을 정확히 지정합니다.


# 골든 크로스와 데드 크로스
# capczrer1-image.png
#
# 이번 토픽에서는 두 개의 이동 평균선을 그리고, 이동 평균선이 교차하는 지점에서 주식을 사고파는 식으로 진행해 볼 건데요.
# 혹시 주식에서 골든 크로스, 데드 크로스라는 용어를 들어 보신 분들도 있을 겁니다.
#
# 짧은 이동 평균선(예를 들면 MA20)이 더 긴 이동 평균선(예를 들면 MA60)을
# 상승하면서 돌파한다면,
# 골든 크로스라고 부르고 주식 가격의 상승 시그널로 해석합니다.
#
# 반대로 짧은 이동 평균선이 긴 이동 평균선을 하락하면서 돌파한다면
# 데드 크로스라고 부르고 하락 시그널로 해석합니다.
#
# 이동 평균선 매매 전략
# 이번 토픽에서는 파이썬으로 자동 매매를 해 볼 건데요.
# 골든 크로스와 데드 크로스를 활용해서 골든 크로스가 나타나면 주식을 매수하고
# 데드 크로스가 나타나면 주식을 매도하는 전략을 취할 겁니다.
# 이걸 개념을 코드처럼 표현한 의사 코드(pseudo code)로 전략만 써 본다면
# 이렇게 쓸 수 있을 거예요.
#
#
# if MA20 값이 MA60 보다 작았다가 커진 경우:
#     매수 신호
# else if MA20 값이 MA60 보다 컸다가 작아진 경우:
#     매도 신호
# 이 코드를 보다 정확하게 파이썬으로 표현한다면 이렇게 코딩할 수 있습니다.
# 아래 코드를 보기 전에 혼자서 먼저 생각해 보셔도 좋습니다. ma20이랑 ma60이라는 리스트에 각각 이동 평균선 값이 있다고 할 때, 인덱스 i에 해당하는 시점에서는 아래처럼 매매 전략을 판단할 수 있을 겁니다.
#
#
# if ma20[i-1] < ma60[i-1] and ma20[i] >= ma60[i]:
#     # 매수 신호
# elif ma20[i-1] >= ma60[i-1] and ma20[i] < ma60[i]:
#     # 매도 신호
# 중복된 계산을 줄이기 위해서 코드를 조금만 더 수정해 본다면 아래와 같이 정리할 수도 있을 거예요.
#
#
#
# prev = ma20[i-1] - ma60[i-1]
# current = ma20[i] - ma60[i]
#
# if prev < 0 and current >= 0:
#     # 매수 신호
# elif prev >= 0 and current < 0:
#     # 매도 신호
# 백테스트
# 투자 전략을 짜고 코딩을 하더라도, 이걸 곧바로 주식 투자에 적용하는 건 위험하겠죠. 그래서 보통은 과거 데이터를 가지고 전략을 테스트하는데요. 이런 식으로 테스트하는 걸 백테스트라고 부릅니다.
#
# 예를 들어서 위 전략을 테스트해 본다면 과거 삼성전자의 주가 데이터를 가지고 매수/매도를 한다고 가정하고 원하는 수익률을 확인해 보는 것이죠. 주식 거래에는 수수료와 세금이 있기 때문에 조금이라도 손해보지 않을 만큼 수익률이 나와야 할 겁니다.
#
# 과거의 가격 데이터가 있을 때 처음 시점부터 마지막 시점까지 매매 전략을 실행하면서, 수익률을 계산하는 겁니다. Pseudo code로 대략적으로 표현해 보면 아래와 같을 거예요.
#
#
# 가격_데이터 = [...]
# 잔고 = 10000000
# 수량 = 0
#
# for 처음 시점부터 마지막 시점까지:
#     이동 평균선 계산하기
#     매매 전략 판단하기
#     if 매수 신호:
#         매수를 가정하고 잔고와 수량 변경
#     if 매도 신호:
#         매도를 가정하고 잔고와 수량 변경
#     현재 수익률 계산
# 이렇게 계산된 수익률이 꽤 괜찮게 나온다면 실전에 써먹을 만한 전략이겠죠?