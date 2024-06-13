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
# Step 1: Generate random numbers
import random
def generate_numbers(count):
    # lotto_numbers = []
    # for _ in range(count):
    # if _ not in lotto_numbers:
    # 해당 데이터가 없다면 추가해주고, 이미 존재한다면 넘어간다.
    # 문제점 1 : 중복이 나올경우 리스트 길이값이 짧아진다.
    # lotto_numbers.append(random.randint(1, 45))
    # lotto_numbers.append(random.sample(range(1, 45), count))
    # 해결책 : sample 함수 이용, 코드의 간략화
    # return lotto_numbers

    # 문제점 2 : 아웃풋이 [[20, 22, 1, 28, 38, 40]] 로 출력된다.
    # random.sample 함수의 경우 이미 count개의 고유한 요소를 포함하는 리스트를 반환한다.
    # 따라서 바로 리턴을 해주어야 해결 가능하다.

    return random.sample(range(1, 45), count)


# print(f"중복없는 난수 생성: {generate_numbers(6)}")


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
# Step 2: Draw winning numbers including a bonus number
def draw_winning_number():
    plus_numbers = generate_numbers(6)
    plus_numbers.append(random.sample(range(1, 45), 1)[0])
    # Extract the first element from the list
    # 문제점 : sample함수로 단순히 첫번째 괄호만을 append 하게 되면 이중괄호의 발생
    # 해결책 : 생성한 난수의 첫번째 배열 즉, [0]을 직접 추가하면 해결된다.

    return plus_numbers


# return random.sample(range(1, 45), count)


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

# 나의 문제 해결
# Step 3: Count matching numbers
def count_matching_numbers():
    # 참가자의 번호 생성
    list_1 = generate_numbers(6)
    print("list_1(참가자): " + str(list_1))

    # 주최자의 당첨 번호와 보너스 번호 생성
    list_2 = draw_winning_number()
    print("list_2(주최자): " + str(list_2))
    # 방법 2: common_numbers = []
    # for com in list_1:
    #     if com in list_2:
    #         common_numbers.append(com)
    # return common_numbers

    # 내 번호와 주최자의 일반 당첨 번호 비교
    my_numbers = list_1
    winning_numbers = list_2[:-1]  # 보너스 번호를 제외한 일반 당첨 번호
    bonus_number = list_2[-1]  # 보너스 번호

    # 보너스 번호 일치 여부 확인
    common_numbers = [num for num in my_numbers if num in winning_numbers]

    return common_numbers, bonus_number in my_numbers # 튜플 적용
# return common_numbers, bonus_number in my_numbers
# 이 구문은 파이썬에서 튜플을 사용하여 두 가지 값을 동시에 반환하는 방법입니다.
# 여기서 각각의 값들이 무엇을 의미하는지 설명드리겠습니다.
#
# common_numbers
# 먼저, common_numbers는 변수명이고,
# 코드에서 이 변수는 count_matching_numbers 함수에서
# generate_numbers 함수를 통해 생성된 참가자의 번호와
# draw_winning_number 함수를 통해 생성된 주최자의
# 당첨 번호 사이에서 공통된 번호들을 포함하는 리스트입니다.
#
# bonus_number in my_numbers
# 여기서 bonus_number는 보너스 번호를 나타내는 변수입니다.
# my_numbers는 참가자의 번호들이 담긴 리스트입니다.
#
# in 키워드는 파이썬에서 멤버십 연산자로, 특정 요소가
# 리스트(또는 다른 컬렉션)에 포함되어 있는지 여부를 확인합니다.
# 따라서, bonus_number in my_numbers는 보너스 번호인
# bonus_number가 my_numbers 리스트에 포함되어 있는지를 확인하는 조건식입니다.
# 결과는 불리언 값(True 또는 False)으로 평가됩니다.

# 반환값
# return common_numbers, bonus_number in my_numbers는
# 두 가지 값을 튜플 형태로 반환합니다.
# 즉, common_numbers와 bonus_number in my_numbers의 값을
# 함께 반환합니다.
#
# 첫 번째 값인 common_numbers는 count_matching_numbers
# 함수에서 일치하는 일반 당첨 번호들의 리스트입니다.
# 두 번째 값은 보너스 번호 bonus_number가 참가자의 번호들인
# my_numbers에 포함되어 있는지를 나타내는 불리언 값입니다.
# 이렇게 반환된 튜플은 호출한 함수에서 각각의 값을 받아 처리할 수 있습니다.
# 예를 들어, 이 경우에서는 check 함수에서 count_matching_numbers 함수의
# 반환값을 받아 common_numbers와 bonus_match 변수에 할당하여
# 상금을 판단하는 데 사용할 수 있습니다.


# 코딩 방법 1:
# 단계별 설명:
# 번호 생성: generate_numbers(6) 함수를 사용하여 참가자의 번호 list_1을 생성합니다.
# 출력: 생성된 list_1을 문자열로 변환하여 출력합니다.
# 당첨 번호 생성: draw_winning_number() 함수를 사용하여 주최자의 당첨 번호와 보너스 번호가 포함된 list_2를 생성합니다.
# 출력: 생성된 list_2를 문자열로 변환하여 출력합니다.
# 번호 비교: list_1에서 list_2의 일반 당첨 번호와 일치하는 번호들을 common_numbers 리스트에 저장합니다.
# 보너스 번호 확인: list_2에서 마지막 요소를 보너스 번호로 지정하고, 이 번호가 list_1에 있는지를 확인하여 bonus_match 변수에 저장합니다.
# 반환: common_numbers 리스트와 bonus_match 변수를 튜플로 반환합니다.

# 코딩 방법 2:
# 1. 변수 정의 및 초기화
# common_numbers = []
# common_numbers라는 빈 리스트를 생성합니다.
# 이 리스트는 나중에 공통된 숫자들을 저장할 용도로 사용됩니다.

# 2. 반복문을 통한 요소 비교
# for com in list_1:
#     if com in list_2:
#         common_numbers.append(com)
# for 문을 사용하여 list_1의 각 요소 com에 대해 다음을 수행합니다:
# if com in list_2:: 만약 com이 list_2에 포함되어 있다면 아래의 동작을 수행합니다.
# common_numbers.append(com): com을 common_numbers 리스트에 추가합니다.

# 3. 반환
# return common_numbers
# 반복문이 끝나면 (list_1의 모든 요소에 대해 확인이 끝나면),
# common_numbers 리스트에는 list_1과 list_2에서 공통된 요소들이 저장되어 있습니다.
# common_numbers 리스트를 반환하여 호출된 곳에서 사용할 수 있도록 합니다.

# 동작 요약
# count_matching_numbers 함수는 두 개의 리스트 list_1과 list_2를 받아서 list_1의 각 요소가 list_2에 있는지 확인합니다.
# 공통된 요소들을 common_numbers 리스트에 저장하고, 이를 반환합니다.


# 리스트 슬라이싱
# 1. list_2[:-1]
# list_2[:-1]은 리스트 list_2의 첫 번째부터 마지막에서 두 번째 요소까지를 포함하는 부분 리스트를 만듭니다. 다음과 같이 작동합니다:
#
# : 기호는 전체 범위를 나타냅니다.
# -1은 인덱스를 거꾸로 세는 것으로, 리스트의 끝에서 첫 번째 요소를 나타냅니다. 즉, 마지막 요소의 바로 이전 위치를 의미합니다.
# 예를 들어, list_2가 [10, 20, 30, 40, 50]라고 가정하면:
#
# list_2[:-1]  # 결과는 [10, 20, 30, 40]이 됩니다.
# 2. list_2[-1]
# list_2[-1]은 리스트 list_2의 마지막 요소를 의미합니다. 즉, 리스트의 끝에서 첫 번째 요소를 가리킵니다.
#
# 이해를 돕기 위해 위 예제인 list_2가 [10, 20, 30, 40, 50]일 때:
#
# list_2[-1]  # 결과는 50이 됩니다.

# 사용 예시
# 주로 이런 기법들은 리스트에서 특정 범위의 요소를 추출할 때 유용하게 사용됩니다.
# 예를 들어, list_2[:-1]을 사용하여 보너스 번호를 제외한 일반 당첨 번호를 추출하거나,
# list_2[-1]을 사용하여 보너스 번호를 추출할 수 있습니다.

# 1. common_numbers 생성
# common_numbers = [num for num in my_numbers if num in winning_numbers]
# common_numbers는 리스트 컴프리헨션을 사용하여 생성됩니다.
# my_numbers 리스트의 각 요소 num에 대해 다음을 수행합니다:
# if num in winning_numbers:
# 만약 num이 winning_numbers에 포함되어 있다면,
# num을 common_numbers 리스트에 추가합니다.
# 따라서, common_numbers 리스트에는 my_numbers와
# winning_numbers에서 공통된 요소들이 저장됩니다.

# 2. bonus_number in my_numbers 확인
# bonus_match = bonus_number in my_numbers
# bonus_number: 이는 보너스 번호를 나타내는 변수입니다.
# my_numbers: 이는 참가자의 번호들이 담긴 리스트입니다.
# 이 부분에서 bonus_number in my_numbers는 다음과 같이 작동합니다:
#
# in 키워드는 멤버십 연산자로, 특정 요소가 리스트(또는 다른 컬렉션)에 포함되어 있는지 여부를 확인합니다.
# 따라서, bonus_number in my_numbers는 보너스 번호 bonus_number가 my_numbers 리스트에 포함되어 있는지를 확인합니다.
# 결과는 불리언 값(True 또는 False)으로 반환됩니다.

# 3. 결과 반환
# return common_numbers, bonus_match
# common_numbers: 일치하는 일반 당첨 번호들의 리스트
# bonus_match: 보너스 번호가 참가자의 번호들 중 하나와 일치하는지의 여부를 나타내는 불리언 값



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

# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원

# 나의 문제 해결
# Step 4: Check the prize amount
# def check():
#     if len(count_matching_numbers()) == 3:
#         print(5000)
#     elif len(count_matching_numbers()) == 4:
#         print(50000)
#     elif len(count_matching_numbers()) == 5:
#         print(1000000)
#     elif len(count_matching_numbers()) == 5 and :
#         print(50000000)
#     elif len(count_matching_numbers()) == 6:
#         print(1000000000)
#     else:
#         print(0)

def check():
    # count_matching_numbers 함수를 통해 결과 가져오기 (튜플 적용)
    common_numbers, bonus_match = count_matching_numbers()
    # count_matching_numbers() 함수를 호출하여 그 결과를 common_numbers와 bonus_match 변수에 할당합니다.
    # count_matching_numbers() 함수는 두 가지 값을 반환하는데,
    # 첫 번째는 common_numbers로 일치하는 일반 당첨 번호들의 리스트이고,
    # 두 번째는 bonus_match로 보너스 번호가 참가자의 번호 중 하나와 일치하는지 여부를 나타내는 불리언 값입니다.

    # 공통된 번호의 개수 확인
    match_count = len(common_numbers)
    # len() 함수를 사용하여 common_numbers 리스트의 길이를 확인합니다.
    # common_numbers 리스트에는 count_matching_numbers 함수에서 반환된 일치하는
    # 일반 당첨 번호들이 들어 있습니다.
    # 따라서, match_count 변수에는 참가자의 번호와 주최자의 당첨 번호 중에서
    # 일치하는 번호들의 개수가 저장됩니다.

    # 상금 결정 조건에 따라 출력
    if match_count == 5 and bonus_match: # bonus_match는 true or false 반환한다.
        print(50000000)  # 5개 일치 + 보너스 번호 일치
    elif match_count == 5:
        print(1000000)   # 5개 일치
    elif match_count == 4:
        print(50000)     # 4개 일치
    elif match_count == 3:
        print(5000)      # 3개 일치
    elif match_count == 6:
        print(1000000000)  # 6개 일치
    else:
        print(f"번호 {match_count}개 일치! 당첨되지 않았습니다! 다음 기회를 노려주세요!")  # 그 외의 경우

# 테스트 실행
check()

# 단계별 설명:
# 결과 가져오기:
# count_matching_numbers() 함수를 호출하여
# 반환된 공통된 번호들과 보너스 번호 일치 여부를
# common_numbers와 bonus_match 변수에 저장합니다.

# 공통된 번호 개수 확인:
# common_numbers 리스트의 길이를 통해
# 공통된 번호의 개수인 match_count를 구합니다.

# 상금 결정:
# match_count와 bonus_match를 조건문을 사용하여
# 상금을 결정하고 출력합니다.

# match_count == 5 and bonus_match: 5개 일치
# + 보너스 번호 일치일 경우 5천만 원을 출력합니다.
# match_count == 5: 5개 일치일 경우 100만 원을 출력합니다.
# match_count == 4: 4개 일치일 경우 5만 원을 출력합니다.
# match_count == 3: 3개 일치일 경우 5천 원을 출력합니다.
# match_count == 6: 6개 일치일 경우 10억 원을 출력합니다.
# 그 외의 경우는 0을 출력합니다.

# 이 두 함수를 함께 사용하면 로또 번호 매칭을 통해 상금을 쉽게 계산할 수 있습니다.
# count_matching_numbers 함수는 번호 매칭을 확인하고 보너스 번호 일치 여부를 반환하며,
# check 함수는 이 정보를 바탕으로 상금을 출력합니다.
