numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# sorted
new_list = sorted(numbers)  # 오름차순 정렬
print(new_list)
new_list = sorted(numbers, reverse=True)  # 내림차순 정렬
print(new_list)

print(numbers)
# 리스트 그대로의 내용이 출력된다.
# sorted 함수는 기존의 리스트를 건들지 않는다.

print(numbers.sort())  # 출력값 None
# sort는 아무것도 return하지 않는다.
# 대신 리스트 자체를 정렬한다.
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# 정리
# sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬

print()
print()
print("=== 실습1 ===")
# 실습 1 설명
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
# greetings 리스트의 원소를 모두 출력하는 프로그램을 작성해 보세요.
# while문과 리스트의 개념을 활용하시면 됩니다.
#
# 출력하면 아래와 같은 결과물이 나와야 합니다.
# 출력 결과
# 안녕
# 니하오
# 곤니찌와
# 올라
# 싸와디캅
# 헬로
# 봉주르

# 나의 문제 해결
print(len(greetings))
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1

# 해설
# 리스트의 인덱스는 1이 아니라, 0부터 시작한다는 걸 유의해 주세요.
#
# greetings 리스트의 원소를 모두 출력하려면 인덱스 0부터 인덱스 6까지의 요소들을 받아오면 되겠죠?
# 그러니가 greetings[0], greetings[1], greetings[2]...
# 이런 식으로 greetings[6]까지 출력하면 된다는 거죠.
#
# 이것을 반복문으로 하면 이렇습니다.

# i = 0
# while i < 7:
#     print(greetings[i])
#     i += 1
# 위 코드를 조금 더 일반화하고 싶으면, len 함수를 쓰면 됩니다.

# 모범 답안
# i = 0
# while i < len(greetings):
#     print(greetings[i])
#     i += 1
# 7이라는 고정값 대신 len(greetings) 같은
# 일반화된 방식으로 쓰면, 더 안정적이고 확장성 있는 코드가 됩니다.


# 실습 2 설명
# 화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.
#
# 섭씨와 화씨의 관계식은 다음과 같습니다:
# °C = (°F−32) ∗ 5 / 9
#
# 화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요.
# 이 함수는 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.

# 실습 결과
# 화씨 온도 리스트: [40, 15, 32, 64, -4, 11]
# 섭씨 온도 리스트: [4.4, -9.4, 0.0, 17.8, -20.0, -11.7]

# 나의 문제 해결
print()
print("=== 실습2 ===")
temperature_list = [40, 15, 32, 64, -4, 11]
print(f"화씨 온도 리스트: {temperature_list}")


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

print(f"섭씨 온도 리스트: {temperature_list}")

# 해설
# 온도 변환 함수
# 화씨 온도를 섭씨 온도로 변환해 주는
# fahrenheit_to_celsius 함수는 이렇게 작성할 수 있습니다.
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
# 한 번 이 함수를 활용해 봅시다. temperature_list에는 화씨 온도가 저장되어 있는데요.
# 만약 2번 인덱스의 원소를 섭씨 온도로 바꾸고 싶다면 뭘 해야 할까요?
#
# 이렇게 하면 됩니다.
# temperature_list[2] = fahrenheit_to_celsius(temperature_list[2])
# 그리고 만약 변환된 섭씨 온도를 소수점 첫째 자리까지 반올림하고 싶다면 이렇게 하면 되겠죠.
# temperature_list[2] = round(fahrenheit_to_celsius(temperature_list[2]), 1)

# 리스트의 모든 요소 변환
# 이제 temperature_list의 모든 원소를 섭씨로 변환하겠습니다. 반복문을 사용해야겠죠?
# 인덱스 0부터 인덱스 len(temperature_list) - 1까지 반복을 해야 하는데요.
# i = 0
# while i < len(temperature_list):
#     # 인덱스 i에 있는 요소 변환
#     i += 1
# 이렇게 하면 되겠네요.
#
# 이제 temperature_list의 인덱스 i에 있는 요소를
# 화씨에서 섭씨로 변환하면 코드가 완성됩니다.

# 모범 답안
# # 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
#
#
# temperature_list = [40, 15, 32, 64, -4, 11]
# print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력
#
# # 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
# i = 0
# while i < len(temperature_list):
#     temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
#     i += 1
#
# print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력

print()
print()

# 실습 3 설명
# 제가 구매하고 싶은 물건들의 가격을 리스트에 정리해 놨습니다.
# prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# 가격의 단위는 모두 원화(￦)인데요. 이 물건들의 가격을 미국 달러($)로 하면 얼마일지,
# 그리고 일본 엔화(￥)로 하면 얼마일지 확인해 보려고 합니다.

# 해야 할 일
# 우리가 해야 할 일은 크게 두 가지입니다.
#
# 함수 작성
# 반복문을 통해 리스트 요소들 변환
# 1. 함수 작성
# 먼저 한국 원화를 미국 달러로 변환해 주는 krw_to_usd 함수,
# 그리고 미국 달러를 일본 엔화로 변환해 주는 usd_to_jpy 함수를 써야 하는데요.
# krw_to_usd 함수는 파라미터로 원화 krw을 받아서 변환된 미국 달러 액수를 리턴해 줍니다.
# 마찬가지로 usd_to_jpy 함수는 파라미터로 달러 usd를 받아서 변환된 일본 엔화 액수를
# 리턴해 주는 거죠.
#
# 참고로 환율은 1달러에 1,000원, 그리고 1,000엔에 8달러라고 가정합니다.
#
# 2. 반복문을 통해 리스트 요소들 변환
# 반복문을 사용해서 리스트의 요소들을 각각 다른 화폐로 변환해야 하는데요.
# 그 과정에서 krw_to_usd 함수와 usd_to_jpy 함수를 활용하면 되겠죠?

# 실습 결과
# 한국 화폐: [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# 미국 화폐: [34.0, 13.0, 5.0, 21.0, 1.0, 2.0, 8.0, 3.0]
# 일본 화폐: [4250.0, 1625.0, 625.0, 2625.0, 125.0, 250.0, 1000.0, 375.0]

# 나의 문제 해결
print("=== 실습3 ===")


# j = 0
# print(len(prices))
def krw_to_usd(krw):
    return krw / 1000


def usd_to_jpy(usd):
    return usd / 8 * 1000


prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print(f"한국 화폐: {prices}")
i = 0
while i < len(prices):
    prices[i] = round(krw_to_usd(prices[i]), 1)
    i += 1

print(f"미국 화폐: {prices}")

i = 0
while i < len(prices):
    prices[i] = round(usd_to_jpy(prices[i]), 1)
    i += 1

print(f"일본 화폐: {prices}")

# 해설
# 함수 정의
# 원화(￦)에서 달러($)로
# krw_to_usd 함수부터 정의합시다.
# 이 함수는 원화를 달러로 변환하는 역할을 하는데요.
# 1,000원은 1달러와 동일합니다.

# 원화(￦)에서 달러($)로 변환하는 함수
# def krw_to_usd(krw):
#     return krw / 1000  # 1,000원 당 1달러

# 달러($)에서 엔화(￥)로
# 마찬가지로 usd_to_jpy는 이렇게 쓸 수 있습니다.

# 달러($)에서 엔화(￥)로 변환하는 함수
# def usd_to_jpy(usd):
#     return usd / 8 * 1000

# 함수 이용하기
# 우리가 정의한 함수를 이용해서 리스트의 원소를 어떻게 수정할 수 있을까요?
# 예를 하나 들어 봅시다.
#
# 인덱스 2의 값을 원화에서 달러로 변환하기 위해서는 이렇게 하면 됩니다.
#
# prices[2] = krw_to_usd(prices[2])
# 만약 변환된 달러를 정수형로 딱 떨어지게 하고 싶으면 이렇게 하면 되고,
#
# prices[2] = int(krw_to_usd(prices[2]))
# 소수점 첫째 자리까지 반올림하고 싶으면 이렇게 하면 됩니다.
#
#
# prices[2] = round(krw_to_usd(prices[2]), 1)
# 반복문으로 모든 원소 변환하기
# 우리가 정의한 함수들과 while 반복문을 사용해서, 리스트의 요소들을
# 각각 다른 화폐로 변환해야 하는데요. 반복문은 인덱스 0부터
# 인덱스 len(prices) - 1까지 돌면 됩니다.
#
# 원화(￦)에서 달러($)로
#
# # prices를 원화(￦)에서 달러($)로 변환하기
# i = 0
# while i < len(prices):
#     prices[i] = krw_to_usd(prices[i])
#     i += 1
#
# # 달러($)로 각각 얼마인가요?
# print("미국 화폐: " + str(prices))
# 달러($)에서 엔화(￥)로
#
# # prices를 달러($)에서 엔화(￥)로 변환하기
# i = 0
# while i < len(prices):
#     prices[i] = usd_to_jpy(prices[i])
#     i += 1
#
# # 엔화(￥)로 각각 얼마인가요?
# print("일본 화폐: " + str(prices))


# 모범 답안
#
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000  # 1,000원 당 1달러


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd / 8 * 1000


# 원화(￦)로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# prices를 원화(￦)에서 달러($)로 변환하기
i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)로 변환하기
i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

# 엔화(￥)로 각각 얼마인가요?
print("일본 화폐: " + str(prices))
#
# 한국 화폐: [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# 미국 화폐: [34.0, 13.0, 5.0, 21.0, 1.0, 2.0, 8.0, 3.0]
# 일본 화폐: [4250.0, 1625.0, 625.0, 2625.0, 125.0, 250.0, 1000.0, 375.0]
