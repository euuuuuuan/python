# 실습 설명
# 이번 실습은 코드잇 실행기가 지원되지 않습니다. 자신의 컴퓨터에서 실습을 진행하고, 셀프 채점 버튼을 눌러 채점해 보세요.
# 앞선 실습에서 프로젝트에 필요한 함수들을 모두 작성했습니다. 지금까지 우리가 작성한 함수는 아래와 같은데요.
#
# generate_numbers(): 무작위로 정답 번호 3개를 뽑는 함수
# take_guess(): 유저에게 번호 3개를 입력 받는 함수
# get_score(): 유저 번호 3개와 정답 번호 3개를 비교해서, 스트라이크와 볼의 개수를 계산하는 함수
# 이제 이 함수들을 활용해서 숫자 야구 게임을 완성합시다.
#
# 실습 결과
#
# 0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.
#
# 숫자 3개를 하나씩 차례대로 입력하세요.
# 1번째 숫자를 입력하세요: 2
# 2번째 숫자를 입력하세요: 2
# 중복되는 숫자 입니다. 다시 입력하세요.
# 2번째 숫자를 입력하세요: 11
# 범위를 벗어나는 숫자입니다. 다시 입력하세요.
# 2번째 숫자를 입력하세요: 3
# 3번째 숫자를 입력하세요: 8
# 1S 1B
#
# 숫자 3개를 하나씩 차례대로 입력하세요.
# 1번째 숫자를 입력하세요: 8
# 2번째 숫자를 입력하세요: 2
# 3번째 숫자를 입력하세요: 0
# 1S 2B
#
# 숫자 3개를 하나씩 차례대로 입력하세요.
# 1번째 숫자를 입력하세요: 2
# 2번째 숫자를 입력하세요: 8
# 3번째 숫자를 입력하세요: 0
# 3S 0B
#
# 축하합니다. 3번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.
import random


def generate_numbers():
    computer_ball = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return random.sample(computer_ball, 3)


print(f"0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다. {generate_numbers()}")


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    count = 1
    while len(new_guess) < 3:
        num = input(f"{count}번째 숫자를 입력하세요: ")

        if num == 'exit' or 'EXIT' or 'Exit':
            print("게임을 종료합니다.")
            return None

        num = int(num)
        if num > 9 or num < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif num in new_guess:
            print("중복되는 숫자 입니다. 다시 입력하세요.")
        else:
            new_guess.append(int(num))
            count += 1

    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif (guesses[i] != solution[i]
              and guesses[i] in solution):
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    guess = take_guess()
    strike, ball = get_score(ANSWER, guess)
    print(f"{strike}S {ball}B")
    tries += 1

    if strike == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
        break


# 해설
# 우리가 써야 하는 코드의 틀을 먼저 구성해 봅시다.
#
# 필요한 변수와 상수를 정의한다.
# 반복적으로 유저에게 번호를 입력 받는다. 만약 스트라이크가 3개 나오면 게임을 종료한다.
# 몇 번만에 맞혔는지 축하 메시지를 출력한다.
# 변수, 상수 정의
# 먼저 필요한 변수와 상수가 무엇인지 생각해 봅시다.
#
# 정답 리스트
# 시도 횟수 (0부터 시작)
# 아래 코드처럼 작성하면 됩니다.
#
#
# ANSWER = generate_numbers()
# tries = 0
# 유저 입력 받기
# 우리가 반복적으로 해야 하는 것들을 정리해 봅시다.
#
# 유저에게 번호 3개를 입력 받는다.
# 스트라이크와 볼의 개수를 센다.
# *S *B의 형태로 스트라이크와 볼의 개수를 출력한다.
# 시도 횟수를 1 늘린다.
# 만약 스트라이크가 3개 나오면 반복문을 종료한다.
# 코드로 작성하면 이렇습니다.
#
#
# while True:
#     user_guess = take_guess()
#     s, b = get_score(user_guess, ANSWER)
#
#     print("{}S {}B\n".format(s, b))
#     tries += 1
#
#     if s == 3:
#         break
# 보시다시피 while문의 조건 부분을 True라고 직접 입력했는데요. 그래서 항상 수행 부분에 들어가게 됩니다. 하지만 s가 3인 경우에는 break문을 수행하기 때문에, while 반복문을 빠져나오게 됩니다. 조건 부분에 s != 3을 입력해도 되는데, 왜 이렇게 작성했을까요? 조건 부분을 s != 3로 하기 위해서는 s가 미리 정의되어 있어야 합니다. 이 방법이 번거롭고 코드도 늘어나서, 위와 같은 방식을 택했습니다.
#
# 축하 메시지 출력
# 반복문을 나온 후에는 축하 메시지를 출력하면 됩니다. tries 변수를 이용해서 몇 번 만에 맞혔는지 알려 주는 것도 잊지 마세요!
#
#
# print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞히셨습니다.".format(tries))
# 모범 답안
#
# from random import randint
#
#
# def generate_numbers():
#     numbers = []
#
#     while len(numbers) < 3:
#         new_number = randint(0, 9)
#         if new_number not in numbers:
#             numbers.append(new_number)
#
#     return numbers
#
#
# def take_guess():
#     new_guess = []
#     while len(new_guess) < 3:
#         num = int(input("{}번째 수를 입력하세요: ".format(len(new_guess) + 1)))
#
#         if num < 0 or num > 9:
#             print("0에서 9까지의 수를 입력해 주세요!")
#         elif num in new_guess:
#             print("중복되는 숫자입니다. 다시 입력하세요.")
#         else:
#             new_guess.append(num)
#
#     return new_guess
#
#
# def get_score(guesses, solution):
#     strike_count = 0
#     ball_count = 0
#
#     for i in range(3):
#         if guesses[i] == solution[i]:
#             strike_count += 1
#         elif guesses[i] in solution:
#             ball_count += 1
#
#     return strike_count, ball_count
#
#
# # 여기서부터 게임 시작!
# ANSWER = generate_numbers()
# tries = 0
#
# while True:
#     user_guess = take_guess()
#     s, b = get_score(user_guess, ANSWER)
#
#     print("{}S {}B\n".format(s, b))
#     tries += 1
#
#     if s == 3:
#         break
#
# print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞히셨습니다.".format(tries))