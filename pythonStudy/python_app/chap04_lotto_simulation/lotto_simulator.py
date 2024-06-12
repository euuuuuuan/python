# 로또 시뮬레이션 프로그램을 만들어 보겠습니다. 이 프로그램은 과정이 많기 때문에, 여러 파트로 나눠서 문제를 해결해 나갈 건데요. 먼저 이 레슨에서 프로그램 전체에 대해 설명해 드리겠습니다.
#
# 규칙
# 로또는 주 1회 간격으로 당첨자를 발표합니다. 참여 횟수에 제한이 없어서, 한 사람이 한 회차에 여러 번 참여할 수도 있습니다. 고를 수 있는 번호는 1부터 45까지 있는데요. 주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 그리고 참가자는 참여할 때마다 서로 다른 번호 6개를 선택합니다. 당첨 액수는 아래 규칙에 따라 결정됩니다.
#
# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원
# 프로젝트에서 작성할 함수 미리보기
# 여러분의 임무는 로또 시뮬레이션을 위한 함수들을 작성하는 것입니다. 어떤 함수들이 있는지 봅시다.
#
# generate_numbers() 함수
# 이 함수는 파라미터로 정수 n을 받습니다. 1과 45 사이의 서로 다른 번호를 무작위로 n개 뽑고, 그 번호들이 담긴 리스트를 리턴합니다. 예시 코드와 실행 결과를 보여 드릴게요.
#
#
# print(generate_numbers(6))
#
# [16, 2, 30, 40, 15, 33]
# 다시 실행하면 또다른 결과가 나오겠죠? 참고로 이 함수는 참가자의 번호를 뽑는 데에도 쓰이고, 보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.
# 나의 문제 해결
import random


def genderate_numbers(count):
    lotto_numbers = []
    for _ in range(count):
        if _ not in lotto_numbers:  # 해당 데이터가 없다면 추가해주고, 이미 존재한다면 넘어간다.
            lotto_numbers.append(random.randint(1, 45))
    return lotto_numbers


print(genderate_numbers(6))


#  _ 언더바는 보통 반복을 위한 카운터 변수로 사용되는데,
#  해당 변수를 사용하지 않을 때 자리 표시자로 사용됩니다.
#  즉, _ 언더바는 반복되는 값에 관심이 없을 때 사용됩니다.
#
# 예를 들어, range() 함수를 사용하여 일정 범위의 숫자를 생성하고자 할 때,
# 해당 숫자를 사용하지 않는다면 _를 대체할 수 있습니다.
# 아래는 _를 사용하지 않은 예시 코드입니다:
# for i in range(5):
#     print(i)
# 위 코드는 0부터 4까지의 숫자를 출력합니다.
# 그러나 만약 우리가 반복되는 값에 관심이 없고,
# 카운터 변수를 사용하지 않는다면 아래와 같이 _를 사용할 수 있습니다:
# for _ in range(5):
#     print("Hello")
# 위 코드는 "Hello"를 5번 출력합니다.
# 여기서 _는 단순히 반복되는 횟수에 관심이 없음을 나타냅니다.
# 따라서 _ 언더바는 반복하는 동안 사용되는 값을 무시하고자 할 때 흔히 사용됩니다.


# draw_winning_numbers() 함수
# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다.
# 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
# 코드와 실행 결과를 예로 보여 드릴게요.
#
# print(draw_winning_numbers())
#
# [4, 12, 14, 28, 40, 41, 6]
# 앞서 정의한 generate_numbers() 함수를 잘 활용하면, 간결하게 작성할 수 있습니다.
# 나의 문제 해결
def draw_winning_number():
    plus_numbers = genderate_numbers(6)
    plus_numbers.append(random.randint(1, 45))
    return plus_numbers


print(draw_winning_number())


# print(draw_winning_number())

# count_matching_numbers() 함수
# 파라미터로 리스트 list_1과 리스트 list_2를 받고,
# 두 리스트 사이에 겹치는 번호의 개수를 리턴합니다. 아래 코드와 실행 결과를 참고해 주세요.
#
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
#
# 3
# 2, 11, 14, 3개의 숫자가 겹치기 때문에 3이 나왔습니다.
#
# 하나의 예를 더 보여 드릴게요.
#
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
#
# 1
# 이번에는 14, 1개만 겹치기 때문에 1이 나왔습니다.
def count_matching_numbers():
    list_1 = genderate_numbers()
    print(list_1)
    list_2 = genderate_numbers()
    print(list_2)
    common_numbers = []
    for com in list_1:
        if com in list_2:
            common_numbers.append(com)
    return common_numbers

print(len(count_matching_numbers()))

# check() 함수
# 참가자의 당첨 금액을 리턴합니다.
# 파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서
# 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요.
# numbers는 당연히 6개의 번호를 담고 있고,
# winning_numbers는 보너스 번호까지 7개의 번호를 담고 있겠죠?
# 예시를 한번 보여 드릴게요.
#
# numbers_test = [2, 4, 11, 14, 25, 40]
# winning_numbers_test = [4, 12, 14, 28, 40, 41, 6]
#
# print(check(numbers_test, winning_numbers_test))
#
# 5000
# 4, 14, 40, 이렇게 번호 3개가 겹치기 때문에 5천 원에 당첨되었습니다.
