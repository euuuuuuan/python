numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# sorted
new_list = sorted(numbers) # 오름차순 정렬
print(new_list)
new_list = sorted(numbers, reverse=True) # 내림차순 정렬
print(new_list)

print(numbers)
# 리스트 그대로의 내용이 출력된다.
# sorted 함수는 기존의 리스트를 건들지 않는다.

print(numbers.sort()) # 출력값 None
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
print("=== 실습 ===")
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