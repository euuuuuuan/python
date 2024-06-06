# 실습 1 설명
# while문과 if문을 활용하여, 100 이하의 자연수 중
# 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
#
# 예를 들어서 16은 8의 배수이지만 12의 배수가 아니니까 조건에 부합합니다.
# 하지만 48은 8의 배수이면서 12의 배수이기도 해서 조건에 부합하지 않습니다.

# 출력 결과
# 8
# 16
# 32
# 40
# 56
# 64
# 80
# 88

# i = 1
# while i <= 100:
#     if i % 8 == 0 and i % 12 != 0:
#         print(i)
#     i += 1

# 해설
# 1부터 100까지 모든 수를 출력하기 위해서는 이렇게 하면 됩니다.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# 실습 2 설명
# 10보다 작은 2 또는
# 3의 배수는 2, 3, 4, 6, 8, 9이며,
# 이들의 합은 32입니다.
# while문과 if문을 활용하여,
# 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을
# 출력하는 코드를 작성해 보세요.

# 실습 결과
# 333167

# 10보다 작은 2 또는
# 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# 구현 코드가 아래이다.
# i = 1
# while i < 10:
#     if i % 2 == 0 or i % 3 == 0:
#         print(i)
#     i += 1

# 나의 문제 해결
# i = 1
# total = 0
# while i < 1000:
#     if i % 2 == 0 or i % 3 == 0:
#         # print(i)
#         total += i
#     i += 1
#
# print(total)

# 해설
# 문제 단순화하기
# 먼저 '2 또는 3의 배수'라는 조건은 무시하고,
# 그냥 10보다 작은 자연수의 합을 출력하는 코드를 작성해 봅시다.
#
# 10보다 작은 자연수의 합을 출력하는 코드를 작성하기 위해서는
# 누적된 합을 보관하는 변수가 필요한데요.
# 우리는 그 변수를 total이라고 하겠습니다.
# 그러면 이렇게 작성할 수 있습니다.

# i = 1
# total = 0
#
# while i < 10:
#     total += i  # total = total + i와 동일
#     i += 1  # i = i + 1과 동일
#
# print(total)

# 위 코드를 실행하면 45라는 결과가 나옵니다.
# 반복문을 돌면서 매번 total에 i를 더하면 되는 거죠.
# 그리고 반복문이 끝나면 총 누적된 합인 total을 출력하면 됩니다.
# 만약 1,000보다 작은 자연수의 합을 출력하려면,
# 위 코드에서 10을 1000으로 바꾸기만 하면 되겠죠?

# 조건 추가하기
# 이제 위 코드에서 한 줄만 추가하면 되는데요.
# total += 1을 매번 실행하는 게 아니라,
# i가 '2 또는 3의 배수'라는 조건에 부합할 때만 실행하는 것입니다.
# 2 또는 3의 배수인지 판단하기 위해서는,
# 2 또는 3으로 나누어떨어지는지 확인해야 합니다.
# 어떤 수가 2 또는 3으로 나누어떨어진다는 것은,
# 2 또는 3으로 나누었을 때 나머지가 0이라는 의미입니다.
#
# i라는 변수가 2로 나누어떨어지는지 확인하는 코드는 i % 2 == 0입니다.
# i라는 변수가 3으로 나누어떨어지는지 확인하는 코드는 i % 3 == 0입니다.
# 그렇다면 i가 2 또는 3으로 나누어떨어지는지 확인하는 코드는 어떻게 표현할까요?
# 불린 연산 or을 사용해서 i % 2 == 0 or i % 3 == 0, 이렇게 표현하면 됩니다.
#
# 반목문을 다룰 때는 무한 루프에 주의해 주세요.
# 이번 실습에서 i += 1은 if문 밖에 있어야 합니다.

# 실습 3 설명
# 약수는 정수 n을 어떤 수로 나누었을 때 나누어떨어지게 하는 정수를 의미합니다.
# 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 됩니다.
#
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 코드를 작성해 보세요.

# 실습 결과
# 1
# 2
# 3
# 4
# 5
# 6
# 8
# 10
# 12
# 15
# 20
# 24
# 30
# 40
# 60
# 120
# 120의 약수는 총 16개입니다.

# 나의 문제 해결
# i = 1
# N = 120
# count = 0
# while i <= 120:
#     if N % i == 0:
#         print(i)
#         count += 1
#     i += 1
#
# print(f"120의 약수는 총 {count}개입니다.")

# 해설
# 약수 모두 출력하기
# 약수를 세는 것은 일단 미루어 두고, 약수를 모두 출력하는 코드부터 작성해 봅시다.
#
# 120의 약수를 모두 찾아야 하는데요.
# 그러면 120이 1로 나누어떨어지는지 확인하고, 2로 나누어떨어지는지 확인하고,
# 3으로 나누어떨어지는지 확인하고...
# 이런 식으로 120까지 나누어떨어지는지 확인하면 됩니다.
#
# '나누어떨어진다'는 건 코드로 어떻게 나타낼까요?
# 변수 i가 4로 나누어떨어진다면,
# i % 4 == 0은 True가 나올 것입니다.

# N = 120
# i = 1
#
# while i <= N:
#     if N % i == 0:
#         print(i)
#     i += 1

# 반목문을 다룰 때는 무한 루프에 주의해 주세요.
# 이번 실습에서 i += 1은 if문 밖에 있어야 합니다.

# 약수 세기
# 그런데 이 문제에서는 약수를 모두 출력하는 것뿐만 아니라
# 약수의 총 개수도 출력해야 합니다. 그러기 위해서는 개수를 세기 위한
# 변수를 하나 만들어야겠죠? 변수 이름은 count 같은 게 좋을 것 같습니다.
#
# 이 count 변수는 어떻게 활용해야 할까요?
# 120의 약수를 발견했을 때마다 1씩 늘리면 되겠죠?

# N = 120
# i = 1
# count = 0
#
# while i <= N:
#     if N % i == 0:
#         print(i)
#         count += 1
#     i += 1

# 모범 답안
# N = 120
# i = 1
# count = 0
#
# while i <= N:
#     if N % i == 0:
#         print(i)
#         count += 1
#     i += 1
#
# print("{}의 약수는 총 {}개입니다.".format(N, count))

# 실습 4 설명
# while문을 사용해서 구구단을 출력하는 코드를 작성해 봅시다.
#
# 참고로 이 문제는 '중첩 while문'이라는 개념을 사용해야 하는데요.
# 중첩 while문은 while문의 동작 부분 안에 또 다른 while문을 넣는 것을 이야기합니다.
# 앞에서 설명 드리지 않은 개념이지만, 조금 고민하다 보면 여러분이 직접 알아내실 수도 있습니다.
# 도저히 생각이 나지 않는다면 힌트를 참고해 주세요.

# 실습 결과
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
# i = 1  # 앞단
# s = 1  # 뒷단
# total = 0  # 결과값
# while i <= 9:
#     s = 1
#     while s <= 9:
#         total = i * s
#         print(f"{i} * {s} = {total}")
#         s += 1
#     i += 1

    # while s <= N:
    #     i += 1
    #     total = i * s
    #     print(f"{i} * {s} = {total}")

# 해설
# 중첩 while문이라는 개념이 조금 어렵게 느껴지죠?
# 그럼 우선 while문 하나만 사용해서,
# 1 * 1 = 1부터 1 * 9 = 9까지 1단만 출력해 봅시다.

# j = 1
# while j <= 9:
#     print("1 * {} = {}".format(j, 1 * j))
#     j += 1

# 여기서 조금 발전시키면 1단부터 9단까지 출력할 수 있는데요. 아래 코드를 보세요.
# print("{} * {} = {}".format(1, j, 1 * j))
# 지금은 1단이기 때문에 그냥 1로 고정되어 있는 부분들이 있습니다.
# 1단부터 9단까지 출력하기 위해서는 고정된 1이 아니라 바뀌는 변수를 넣어 줘야겠죠?
# 이를 위해 또 다른 while문으로 감싸면 되는 것입니다.

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print("{} * {} = {}".format(i, j, i * j))
#         j += 1
#     i += 1

# 모범 답안
# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print("{} * {} = {}".format(i, j, i * j))
#         j += 1
#     i += 1

# 실습 5 설명
# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만 원을 받았습니다.
#
# 이 돈을 어떻게 할지 고민하던 택이는,
# 이웃인 동일 아저씨와 미란 아주머니의 의견 중 하나를 선택하려 합니다.

# 1. 동일 아저씨 의견
# > 원금에 붙은 이자에 다시 이자가 붙는 연복리 예금에 넣기

#  <연복리 예금 상품 정보>
#
#  원금: 50,000,000 원
#  연 이율: 12%
#  1년 뒤 은행 잔고: 50,000,000 * (1 + 12%) = 56,000,000 원
#  2년 뒤 은행 잔고: 50,000,000 * (1 + 12%) * (1 + 12%) = 62,720,000 원
#  ...

# 상수 정의
# BREAKING_YEAR = 2016
# APARTMENT_RPICE_2016 = 1100000000
# INTEREST_RATE = 0.12
#
# # 변수 정의
# year = 1988  # 연도 (year): 1988부터 2016까지 바뀜
# bank_balance = 50000000  # 은행 잔액 (bank_balance): 50000000으로 시작해서 매년 이자가 쌓임
# # bank_balance = int(bank_balance * (1 + INTEREST_RATE))
# year_after = 0

# while 반복문의 동작 부분에는 몇 번 들어가야 할까요?
#
# 1988년에서 1989년으로 넘어갈 때 이자가 쌓여야겠죠?
# 마찬가지로 1989년에서 1990년으로 넘어갈 때도 이자가 쌓여야 합니다.
# 이런 식으로 2015년에서 2016년으로 넘어갈 때까지 동작 부분으로 들어가서
# 이자가 쌓여야 하는 거죠.


# 나의 문제 해결
# while year < BREAKING_YEAR:
#     year_after += 1
#     bank_balance += bank_balance * (1 + INTEREST_RATE)  # 1년뒤 56,000,000 // 2년뒤 62,720,000
#     year += 1
#     print(f"{year_after}년 뒤 은행 잔고: {int(bank_balance)} 원")
#     # print(bank_balance)
# if bank_balance > APARTMENT_RPICE_2016:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_RPICE_2016)))
# else:
#     print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_RPICE_2016 - bank_balance)))

# while year < BREAKING_YEAR:
#     year_after += 1
#     print(f"{year_after}년 뒤 은행 잔고: {bank_balance} 원")
#     year += 1
#     bank_balance += bank_balance0
#     print(bank_balance)
#     if bank_balance < APARTMENT_RPICE_2016:
#         print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(APARTMENT_RPICE_2016 - bank_balance))
# else:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(bank_balance - APARTMENT_RPICE_2016))
# 2. 미란 아주머니 의견
# > 아파트 가치 상승을 고려하여 당시 매매가 5000만 원인 은마 아파트 사기
# 2016년 기준 은마아파트의 매매가는 11억 원인데요.
# 1988년 은행에 5,000만 원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,
#
# 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.를 출력하고
# 은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다. 를 출력하는 코드를 작성해 보세요.

# 유의사항
# 1. 금액은 정확한 표기를 위해 아래 값을 복사해서 이용하시는 걸 권장합니다.
# 1100000000
# 50000000

# 2. 2016년에 은행에 저축해 둔 금액 계산은 while 문을 이용한 반복문으로 계산해주세요.
# 3. 은마아파트 가격과 은행에 저축해 둔 금액을 비교 후 메시지 출력시에는 if 문을 사용해주세요.
# 4. 최종 결과에서 1원 미만은 계산하지 않습니다.

# 실습 결과
# 94193324원 차이로 동일 아저씨 말씀이 맞습니다.

# 해설
# 상수와 변수
# 먼저 이 프로그램에서 사용될 상수와 변수를 모두 정의해 봅시다.
# 사용될 값들을 미리 적어 두면 틀이 잡힌 상태에서 고민을 시작할 수 있습니다.
# 상수(바뀌지 않을 값)와 변수(바뀔 값)를 나눠서 생각해 봅시다.
# 상수 이름은 모두 대문자로 쓴다는 점 잊지 말아 주세요.
# 먼저 상수는 어떤 것들이 있을까요?

# # 상수 정의
# INTEREST_RATE = 0.12
# APARTMENT_PRICE_2016 = 1100000000

# 이제 변수도 생각해 볼게요.
# 우선 반복문을 돌기 위해 사용되는 변수를 생각해 봅시다.
# 우리는 1988년부터 시작해서 2016년까지 반복을 해야 하는데요.
# 그러면 연도를 나타내는 변수가 필요합니다. year라고 이름을 짓겠습니다.
# 또 어떤 변수가 필요할까요?
# 처음에는 은행에 5,000만 원을 넣었지만, 매년 그 금액이 바뀔 텐데요.
# 이건 bank_balance라는 변수에 저장하겠습니다.
# 정리하자면 이렇습니다.

# 연도 (year): 1988부터 2016까지 바뀜
# 은행 잔액 (bank_balance): 50000000으로 시작해서 매년 이자가 쌓임

# 변수 정의
# year = 1988
# bank_balance = 50000000

# (Python 3.6 버전 이상) 숫자를 천 단위로 나누고 싶을 때 underscore 를 쓸 수 있어요
# APARTMENT_PRICE_2016 = 1_100_000_000
# bank_balance = 50_000_000

# while 반복문
# 반복문을 이용해서 1988년부터 2016년까지 돈이 얼마나 쌓이는지 계산해야 합니다.
# 어떻게 할 수 있을까요?
# while 반복문의 수행 부분에 들어갈 때마다 bank_balance가 12%씩 늘어나도록 하면 되겠죠?
# 코드로 표현하면 이렇습니다.

# bank_balance = bank_balance * (1 + INTEREST_RATE)

# 그런데 수행 부분에 몇 번이나 들어가야 할까요?
# 1988년에서 1989년으로 넘어갈 때 이자가 쌓여야겠죠?
# 마찬가지로 1989년에서 1990년으로 넘어갈 때도 이자가 쌓여야 합니다.
# 이런 식으로 2015년에서 2016년으로 넘어갈 때까지 수행 부분으로 들어가서 이자가 쌓여야 하는 거죠.
# 그러면 반복문을 이렇게 쓸 수 있습니다.

# while year < 2016:
#     bank_balance = bank_balance * (1 + INTEREST_RATE)
#     year += 1

# if, else문
# 마지막으로 결과를 출력하기만 하면 되는데요.
# 은행 잔액이 더 큰지 아파트 가격이 더 큰지에 따라서 출력 결과를 정하면 됩니다.

# if bank_balance > APARTMENT_PRICE_2016:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
# else:
#     print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))

# 모법 답안
# 상수 정의
# INTEREST_RATE = 0.12
# APARTMENT_PRICE_2016 = 1100000000
#
# # 변수 정의
# year = 1988
# bank_balance = 50000000
#
# while year < 2016:
#     bank_balance = bank_balance * (1 + INTEREST_RATE)
#     year += 1
#
# if bank_balance > APARTMENT_PRICE_2016:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
# else:
#     print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))

# 실습 5 설명
# 피보나치 수열(Fibonacci Sequence)이라고 들어 보셨나요?
# 1,1,2,3,5,8,13,21,34,55,...
# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다.
# 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다.
# 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며,
# 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.
#
# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 코드를 작성해 보세요.

# 실습 결과
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# .
# .
# .
# 4807526976
# 7778742049
# 12586269025

# 나의 문제 해결
previous = 0
current = 1
i = 0
while i <= 24:
    print(current) # 1
    previous += current
    print(previous) # 1
    current += previous
    i += 1

# 해설
# 일단 50개의 항이 조금 부담될 수 있으니, 10개의 항만 출력하는 것을 목표로 합시다.
# 어차피 10개를 제대로 출력할 수 있으면, 50개도 아무런 문제없이 출력할 수 있을 테니까요.

# 반복문 틀 작성
# 10개의 항을 출력하기 위해서는 반복문을 열 번 돌아야겠죠?
# 열 번 도는 반복문부터 작성해 봅시다.

# i = 1
#
# while i <= 10:
#     i += 1

# 필요한 변수 정의
# 피보나치 수열의 항은 앞선 두 항의 합으로 계산되는데요. 따라서
# 피보나치 수열의 항들을 순서대로 출력하기 위해서는 늘 마지막 두 항을 변수에 보관해야 합니다.
#
# '현재 항'은 변수 current에, 그리고 '직전 항'은 변수 previous에 저장하겠습니다.
# 처음에는 current를 1로 설정하고 previous를 0으로 설정하면 되겠죠?

# previous = 0
# current = 1
# i = 1
#
# while i <= 10:
#     # 우리가 반복적으로 무엇을 해야 할까요?
#     i += 1
# 이제 while 반복문의 동작 부분만 채워 넣으면 됩니다.

# 동작 부분 채워 넣기
# 동작 부분에서 해야 할 일은 크게 두 가지입니다.
# current를 출력
# previous와 current를 적절히 수정
# 첫 번째 내용은 그냥 print(current)를 하면 되니까 먼저 채워 넣겠습니다.

# previous = 0
# current = 1
# i = 1
#
# while i <= 10:
#     print(current)
#     # previous와 current를 적절히 수정
#     i += 1

# previous와 current 수정하기
# 두 번째가 약간 헷갈리는 부분인데요.
# 동작 부분에서 previous와 current를 어떻게 수정할 수 있을까요?
# 일단 단순하게 생각하면 이렇습니다.

# previous ← current
# current ← current + previous

# 그리고 위 로직을 코드로 나타내면 아래와 같습니다.
# previous = current
# current = current + previous

# 그런데 사실 위 코드처럼 하면 문제가 생깁니다.
# 코드의 순서대로 한번 따라가 볼게요.
# previous = current를 하면, previous와 current가 같은 값을 저장하게 됩니다.
# 그리고 기존의 previous 값은 잃어버리게 되죠.
#
# 예를 들어서 previous가 정수 2고 current가 정수 3이라고 생각해 보세요.
# previous = current를 하면 어떻게 되나요?
# previous는 정수 3으로 바뀌고, current도 정수 3이죠? 기존 previous에 있던
# 정수 2는 완전히 잃어버리게 됩니다.
#
# 이 문제를 해결하기 위해서, 임시 보관소 역할을 할 변수를 만들어야 합니다.

# temp = previous  # previous를 임시 보관소 temp에 저장
# previous = current
# current = current + temp  # temp에는 기존 previous 값이 저장돼 있음

# 이렇게 하면 이제 문제없이 previous와 current를 수정할 수 있습니다.
# 코드를 실행하면 아래와 같이 출력이 될 텐데요.

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

# 이제 while i <= 10:을 while i <= 50:으로 수정하기만 하면 됩니다.

# 모범 답안
# previous = 0
# current = 1
# i = 1
#
# while i <= 50:
#     print(current)
#     temp = previous  # previous를 임시 보관소 temp에 저장
#     previous = current
#     current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
#     i += 1

# 참고 사항
# 참고로 이 코드를 더 깔끔하게 쓰는 방법이 있는데요. 아래 코드를 봐 주세요.
# previous = 0
# current = 1
# i = 1
#
# while i <= 50:
#     print(current)
#     previous, current = current, current + previous
#     i += 1
# 훨씬 낫죠? 그런데 제가 굳이 temp를 사용하는 방식을 먼저 말씀드린 이유가 있습니다.
#
# 저렇게 한 줄로 깔끔하게 쓸 수 있는 것은 파이썬에서 제공되는 멋진 문법인데요.
# 코드가 깔끔해지기 때문에 저도 웬만하면 이렇게 작성합니다.
# 하지만 이건 대부분 프로그래밍 언어에서 제공되지 않는 문법입니다.
# 여러분이 이 방식만 배우면, 다른 프로그래밍 언어로는 이 같은 문제를 풀지 못할 수도 있다는 거죠.
# 반면 temp 같은 임시 보관소를 사용하는 방법은 어떤 언어에도 적용 가능하다는 장점이 있습니다.
#
# 그래도 파이썬에서 유용하게 쓸 수 있는 문법임에는 틀림이 없습니다.
# 이 토픽에서는 프로그래밍에서 전반적으로 쓰는 개념들에 집중하고,
# 다른 과제에서 위 방법에 대해 좀 더 살펴보겠습니다.