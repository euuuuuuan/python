my_list = [2, 3, 5, 7, 11]

# number는 for 반복문에서 사용되는 변수
# 0 번 인덱스의 정수 2가 -> 3 -> 5 ...
# for number in my_list:
#     print(number)

# 위 부분과 동일한 동작의 while 문
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# for 문이 더 깔끔하다.
# 상황에 따라 선택해서 문장 구성을 하면 된다.

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(i)

# range 함수
# range() 파라미터 1개
# range( , ) 파라미터 2개
# range( , , ) 파라미터 3개

# 파라미터 1개 버전
# for i in range(stop):
#     print(i)
# -> 0부터 stop-1까지의 범위

# ex) for i in range(10): -> 0~9까지
# -> for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:와 동일

# 파라미터 2개 버전
# for i in range(start, stop):
#     print(i)
# -> start부터 stop-1까지의 범위

# ex) for i in range(3, 11): -> 3~10까지
# -> for i in [3, 4, 5, 6, 7, 8, 9, 10]:과 동일

# 파라미터 3개 버전
# for i in range(start, stop, step):
#     print(i)
# -> start부터 stop-1까지의 범위, 간격 step

# ex) for i in range(3, 17, 3): -> 3~16까지, 숫자들간의 간격
# -> for i in [3, 6, 9, 12, 15]:과 동일

# range 함수 장점?
# 간편함
# 깔끔함
# 메모리 효율성

# 실습 1 설명
# numbers라는 리스트가 주어졌습니다.
#
# for문과 range 함수를 사용하여,
# numbers의 인덱스와 원소를 출력해 보세요.

# numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 실습 결과
#
# 0 2
# 1 3
# 2 5
# 3 7
# 4 11
# 5 13
# 6 17
# 7 19
# 8 23
# 9 29
# 10 31

# 나의 문제 해결
# for i in range(len(numbers)):
#     print(i, numbers[i])

# 해설
# 리스트의 길이가 20이라고 가정하면, 해당 리스트의 인덱스 목록은 range(20)으로 받아올 수 있습니다. 리스트 numbers의 인덱스 목록을 받아오려면 range(len(numbers))를 하면 되겠죠?
#
# 우선 인덱스만 순서대로 출력해 봅시다.
#
#
# for i in range(len(numbers)):
#     print(i)
# 인덱스 i에 있는 원소를 받아오려면 numbers[i]를 하면 되는데요. 그러면 i와 numbers[i]를 함께 출력하면 되겠죠?
#
# 모범 답안
#
# numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#
# # 인덱스와 원소 출력
# for i in range(len(numbers)):
#     print(i, numbers[i])

# 실습 2 설명
# "2의 n제곱"을 출력하는 프로그램을 만들려고 합니다.
#
# 코드를 실행하면 아래와 같이
# 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.
#
# 실습 결과
#
# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# .
# .
# .
# 2^10 = 1024

# 나의 문제 해결
# i = 0
# j = 2
# for i in range(11):
#     result = j ** i
#     print(f"{j}^{i} = {result}")
#     i += 1


# 해설
# "2의 0제곱"부터 "2의 10제곱"까지 출력하고 싶으니까, 0부터 10까지 반복문을 돌리면 되겠죠? 그러면 range(11)을 사용하면 됩니다.
#
#
# for i in range(11):
# 혹시 잊으셨다면, 거듭제곱 연산은 파이썬에서 **인데요. 2 ** 3을 하면 "2의 3제곱"이기 때문에 8이 나오는 거죠.
#
# 이제 거듭 제곱 연산과 문자열 포맷팅을 사용하면 코드를 완성할 수 있습니다.
#
# 모범 답안
#
# for i in range(11):
#     print("{}^{} = {}".format(2, i, 2 ** i))
#
# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# .
# .
# .
# 2^10 = 1024

# 실습 3 설명
# 구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.
#
# 실습 결과
#
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .
# .
# .
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81

# 나의 문제 해결
# i = 1 # 첫째수
# j = 1 # 둘째수
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")

# 해설
# 1단만 작성
# 먼저 1단만 작성하겠습니다.
#
#
# for j in range(1, 10):
#     print("{} * {} = {}".format(1, j, 1 * j))
#
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# 1 * 7 = 7
# 1 * 8 = 8
# 1 * 9 = 9
# 1단부터 9단까지 모두 작성
# while문으로 구구단 만들었던 거 기억 나시나요? 이번에도 매우 유사합니다.
#
# 그때는 while문 안에 또 다른 while문을 "중첩"해서 사용했는데요. 이번에는 for문 안에 또 다른 for문을 쓰셔야 하는 거죠.
#
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{} * {} = {}".format(i, j, i * j))
# 모범답안
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{} * {} = {}".format(i, j, i * j))

# 실습 4 설명
# '피타고라스 정리'라고 들어 보셨나요? 직각삼각형에서,
# 빗변의 제곱이 두 직각변의 제곱의 합과 같다는 정리입니다.
#
# 거기서 나온 '피타고라스 삼조'라는 개념이 있는데요. 피타고라스 삼조란,
# 피타고라스 정리 (a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍 (a,b,c)입니다.
# 예를 들어, 3^2 + 4^2 = 5^2이기 때문에 (3,4,5)는 피타고라스 삼조입니다.
# a < b < c라고 가정할 때, a + b + c = 400을 만족하는 피타고라스 삼조 (a,b,c)는 단 하나인데요.
# 이 경우 a * b * c는 얼마인가요?
# 출력값 : 2040000

# 나의 문제 해결
# for a in range(1, 400):
#     for b in range(1, 400):
#         c = 400 - a - b
#         if a ** 2 + b ** 2 == c ** 2 and a < b < c and a + b + c == 400:
#             print(a * b * c)

# 힌트 1
#
# 가장 단순하게 코드를 짜면 이렇습니다.
#
# for a in range(1, 400):
#     for b in range(1, 400):
#         for c in range(1, 400):
#             if a * a + b * b == c * c and a < b < c and a + b + c == 400:
#                 print(a * b * c)
# 이 코드를 막상 실행해 보면, 굉장히 오랜 시간이 걸릴 것입니다. 논리적으로 봤을 때는 정답을 찾아 주는 코드입니다. 하지만 너무 오래 걸려서 사실상 사용할 수 없다고 보시면 되는데요. 이런 걸 "비효율적인 알고리즘"이라고 합니다.
#
# 알고리즘이 비효율적인 이유를 간단히만 설명드리겠습니다.
#
# a가 가능한 경우는 1부터 399까지, b가 가능한 경우는 1부터 399까지, c가 가능한 경우는 1부터 399까지인데요. 그러면,
#
# if a * a + b * b == c * c and a < b < c and a + b + c == 400:
#     print(a * b * c)
# 위 코드가 총 63,521,199번 실행됩니다. 6천만 번 이상 실행되는 거죠.
#
# 더 효율적인 코드를 짜기 위해서 for문을 두 개만 쓰세요.

# 해설
# 가장 단순한 방식
# 가장 단순하게 코드를 짜면 이렇습니다.
#
#
#
# for a in range(1, 400):
#     for b in range(1, 400):
#         for c in range(1, 400):
#             if a * a +  b * b == c * c and a < b < c and a + b + c == 400:
#                 print(a * b * c)
#
#
#
# 이 코드를 막상 실행해 보면, 꽤 오랜 시간이 걸릴 것입니다. 논리적으로 봤을 때 언젠가는 올바른 정답을 찾아 주는 코드입니다. 하지만 400 대신 더 큰 숫자가 들어갈 수도 있는 걸 감안하면, 너무 오래 걸려서 사실상 사용할 수 없다고 보시면 되는데요. 이런 걸 "비효율적인 알고리즘"이라고 합니다.
#
#
#
# 알고리즘이 비효율적인 이유를 간단히만 설명드리겠습니다.
#
#
#
# a가 가능한 경우는 1부터 399까지, b가 가능한 경우는 1부터 399까지, c가 가능한 경우는 1부터 399까지인데요. 그러면,
#
#
#
# if a * a + b * b == c * c and a < b < c and a + b + c == 400:
#     print(a * b * c)
# 위 코드가 총 63,521,199번 실행됩니다. 6천만 번 이상 실행되는 거죠.
#
# 효율적인 방식
# 우리는 a + b + c = 400이라는 조건을 지켜야 합니다. 그말인즉슨 c = 400 - a - b 입니다.
#
# 모범 답안
# for a in range(1, 400):
#     for b in range(1, 400):
#         c = 400 - a - b
#         if a * a + b * b == c * c and a < b < c:
#             print(a * b * c)
#
#
# 이렇게 하면 정답인 2040000를 구할 수 있습니다.

# 실습 5 설명
# 리스트 내 요소들의 순서를 거꾸로 뒤집으려고 합니다.
#
# 예를 들면 다음과 같습니다.
#
# [1, 4, 7]이 있으면 1과 7의 위치를 바꾸어서 [7, 4, 1]로 만듭니다.
# [1, 4, 7, 11]이 있으면 1과 11의 위치를 바꾸고, 4와 7의 위치를 바꾸어서 [11, 7, 4, 1]로 만듭니다.
# 아래와 같이 numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!
#
#
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#
# # 리스트 뒤집기
# # 여기에 코드를 작성하세요
#
# print("뒤집어진 리스트: {}".format(numbers))
# 실습 결과
#
# 뒤집어진 리스트: [19, 17, 13, 11, 7, 5, 3, 2]
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # left 0 -> 1 -> 2 -> 3...
    right = len(numbers) - left - 1  # 인덱스 left와 대칭인 인덱스 right 계산
    # right 7 -> 6 -> 5 -> 4...
    numbers[right], numbers[left] = numbers[left], numbers[right]  # 위치 바꾸기
    # print(numbers) 이해 돕기용 프린트
    # numbers 배열의 위치 바꾸기

print(f"뒤집어진 리스트: {numbers}")

# 기초강의에서 배우진 않지만, 튜플이라는 자료형이 있습니당.
#
# 리스트는 대괄호를 쓰게되는데, 튜플에서는 소괄호를 쓰게 됩니다.
#
# (값1, 값2, 값3...)
#
# 위처럼 괄호와 comma 를 이용해 표기하게 되어요.
#
# 그런데 이 괄호를 쓰지 않고
#
# 값1, 값2
# 와 같이 쓰더라도 튜플로 인식을 하게 됩니다.
#
# 즉 아래와 같습니다.
#
# numbers1 = (1, 2)
# print(type(numbers1))    # <class 'tuple'>
# numbers2 = 1, 2
# print(type(numbers2))    # <class 'tuple'>
#
# 그럼 = 을 기준으로 우측의 numbers[left], numbers[right]가
# 튜플이 된다는 것은 위로써 설명이 될 것입니다.
# 그리고 또 설명해야 할 것은 unpacking 입니다.
#
# numbers = [1, 2, 3]
# a, b, c, = numbers
# print(a, b, c)    # 1, 2, 3
# 위 코드를 보시게 되면 numbers 의 각 요소들이 하나씩 a, b, c 에 할당되게 되는데
# 이런걸 unpacking 이라고 부릅니다.
#
# numbers[right], numbers[left] = numbers[left], numbers[right] 도 unpacking 과 같습니다.
# numbers[right] 에 numbers[left]를 할당하고 numbers[left]에 numbers[right]를 할당하는 Unpacking 을 진행하는 것이에요.

# 이렇게 unpacking 을 하게 되면 결국 자리바꿈을 한 것과 동일한 결과가 나오는 것입니다.

# 해설
# 접근법 #1
# 리스트를 뒤집기 위해서는, 서로 대칭인 원소들의 위치를 바꿔야(swap) 합니다.
#
# 대칭 관계 이해하기
# 대칭인 원소들을 어떻게 찾을 수 있을까요? 서로 대칭이 되는 인덱스를 찾아야겠죠.
#
# 인덱스 0과 대칭되는 위치는 인덱스 len(numbers) - 1입니다.
# 인덱스 1과 대칭되는 위치는 인덱스 len(numbers) - 2입니다.
# 인덱스 2와 대칭되는 위치는 인덱스 len(numbers) - 3입니다.
# 대칭되는 두 인덱스를 left와 right라고 합시다.
#
# right = len(numbers) - left - 1로 관계를 표현할 수 있습니다.
#
# 반복문 돌기
# 반복문을 돌면서 left 요소와 right 요소의 위치를 바꿔 줘야 합니다.
#
# 그러기 위해서는 이렇게 할 수 있는데요.
#
#
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#
# # 리스트 뒤집기
# for left in range(len(numbers)):
#     # 인덱스 left와 대칭인 인덱스 right 계산
#     right = len(numbers) - left - 1
#
#     # 위치 바꾸기
#     temp = numbers[left]
#     numbers[left] = numbers[right]
#     numbers[right] = temp
#
# print("뒤집어진 리스트: " + str(numbers))
#
# 뒤집어진 리스트: [2, 3, 5, 7, 11, 13, 17, 19]
# 이렇게 하면 리스트가 뒤집히지 않은 상태로 출력됩니다. 왜 그런 걸까요?
#
# 우리는 for문을 left가 0일 때부터 left가 len(numbers) - 1일 때까지 반복하는데요. 사실 left가 그렇게 끝까지 돌 필요가 없습니다. 그냥 리스트 길이의 반만 돌아도 리스트를 뒤집을 수 있기 때문이죠!
#
# 오히려 리스트 길이의 반을 넘게 돌면, 잘 바꿔 놨던 위치를 다시 원상 복구하는 셈입니다. 이미 바뀐 위치에 다시 위치 바꾸기 코드를 적용하게 되니까요. 그래서 리스트 길이의 반만 돌 수 있도록 아래와 같이 작성해주셔야 합니다.
#
#
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#
# # 리스트 뒤집기
# for left in range(len(numbers) // 2):
#     # 인덱스 left와 대칭인 인덱스 right 계산
#     right = len(numbers) - left - 1
#
#     # 위치 바꾸기
#     temp = numbers[left]
#     numbers[left] = numbers[right]
#     numbers[right] = temp
#
# print("뒤집어진 리스트: " + str(numbers))
# 접근법 #2
# 위치 바꾸기를 쉽게 할 수 있는 방법도 알아보겠습니다. 피보나치 수열 과제에서 언급한 방법 기억나시나요? 강의에서 배우지는 않지만, 튜플(tuple)이라는 자료형을 이용해서 할당하는 겁니다. 튜플은 아래와 같이 표현합니다.
#
#
# korean_names = ('효선', '유신')
# english_names = 'hyoseon', 'yusin'
#
# print(type(korean_names))
# print(type(english_names))
#
# <class 'tuple'>
# <class 'tuple'>
# 위처럼 괄호를 통해 표현할 수도 있지만 , 로만 각 요소를 구분해도 튜플로 인식이 됩니다.
#
# 그럼 어떻게 위치를 쉽게 바꿀 수 있는지 코드를 보겠습니다.
#
#
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#
# # 리스트 뒤집기
# for left in range(len(numbers) // 2):
#     # 인덱스 left와 대칭인 인덱스 right 계산
#     right = len(numbers) - left - 1
#
#     # 위치 바꾸기
#     numbers[right], numbers[left] = numbers[left], numbers[right]
#
# print("뒤집어진 리스트: " + str(numbers))
# 위와 같이 쓰게 되면 지정 연산자(=) 의 오른쪽에 있는 튜플이 위치가 바뀌기 전의 numbers[left], numbers[right] 의 값을 보관하게 됩니다. 그리고 numbers[right], numbers[left] 에 해당하는 요소에 값을 각각 할당하게 되면서 이전 코드처럼 임시 변수를 만들지 않고도 값을 교환할 수 있는 것입니다.
#
# 어느 접근법을 이용하여 해결하셔도 좋습니다. 두번째 접근법은 파이썬스러운(Pythonic) 방법으로 다른 코드에서 보실 수도 있으니 참고로 알아두세요!
#
# 모범 답안
#
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#
# # 리스트 뒤집기
# for left in range(len(numbers) // 2):
#     # 인덱스 left와 대칭인 인덱스 right 계산
#     right = len(numbers) - left - 1
#
#     # 위치 바꾸기
#     temp = numbers[left]
#     numbers[left] = numbers[right]
#     numbers[right] = temp
#
# print("뒤집어진 리스트: " + str(numbers))