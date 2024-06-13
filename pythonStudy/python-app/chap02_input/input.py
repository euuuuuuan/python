# name = input("이름을 입력하세요: ")
# print(name)

# x = int(input("숫자를 입력하세요: "))
# 정수형과 문자열은 덧셈이 불가하다. 형변환 필요
# print(x + 5)

# 실습 1 설명

# 1과 20 사이의 숫자를 맞히는 게임을 만들려고 합니다.
# random 모듈과 input() 함수를 활용하여 프로그램을 만들어 보세요.
#
# 진행 방식
# 프로그램을 실행하면 기회가 *번 남았습니다.
# 1-20 사이의 숫자를 맞혀 보세요:가 출력됩니다.
# 총 네 번의 기회가 주어지며,
# 사용자가 한 번 추측할 때마다 남은 기회가 줄어듭니다.
# 정답을 맞히면 축하합니다.
# *번 만에 숫자를 맞히셨습니다.가 출력되고 프로그램은 종료됩니다.
# 사용자가 입력한 수가 정답보다 작은 경우 Up이 출력되고,
# 입력한 수가 정답보다 큰 경우 Down이 출력됩니다.
# 정답이 틀렸으면 1번부터 다시 진행합니다.
# 만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, 아쉽습니다.
# 정답은 *입니다.가 출력되고 프로그램은 종료됩니다.

# 나의 문제 해결
import random
ANSWER = random.randint(1, 20) # 1에서 20 사이의 정수
LIFE = 4 # 시도 가능한 횟수
print(ANSWER) # 답 공개 테스트
guess = 0

while LIFE != 0 and ANSWER != guess:
    guess = int(input(f"기회가 {LIFE}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if guess == ANSWER:
        print(f"축하합니다. {LIFE}번만에 숫자를 맞히셨습니다.")
    elif guess < ANSWER:
        LIFE -= 1
        print("Up")
    elif guess > ANSWER:
        LIFE -= 1
        print("Down")

    if guess > 20:
        LIFE += 1
        print("잘못된 값을 입력하셨습니다. 1-20 사이의 숫자를 맞혀 보세요! ")


    if LIFE == 0:
        print(f"아쉽습니다. 정답은 {ANSWER}였습니다.")


# 해설
# 우선 게임이 실행되는 동안 바뀌지 않을 상수 두 개를 먼저 정의하겠습니다.
#
# 게임의 정답: ANSWER
# 총 기회 수: NUM_TRIES
# 게임이 실행되는 도중에는 정답이 바뀌지 않지만, 다른 게임이 시작되면 정답은 바뀌어야 하죠? random 모듈의 randint() 함수를 사용할게요.
#
#
# import random
#
# ANSWER = random.randint(1, 20)
# 그리고 사용자에게 네 번의 기회를 주고 싶으니까 NUM_TRIES는 4로 설정하겠습니다.
#
#
# NUM_TRIES = 4
# 사용자 인풋 받기
# 이제 사용자에게 인풋을 받아 봅시다. 사용자로부터 입력을 받기 위해서는 아래 코드를 쓰면 되는데요.
#
#
# input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(tries))
# 사용자의 입력을 받는 input() 함수의 리턴값은 문자열입니다. 우리는 문자열이 아닌 정수형을 원하기 때문에, input() 함수의 리턴값을 정수형으로 변환해야 합니다. 그리고 이 정수값을 guess라는 변수에 저장합시다.
#
#
# guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(tries)))
# 위 코드를 while문의 수행 부분에 넣어야 할 텐데요. while문의 조건 부분과 수행 부분은 어떻게 쓰면 좋을지 고민해 보세요.
#
# while문의 조건 부분
# while문의 수행 부분에 들어간다는 것은 어떤 의미인가요? 아직 게임이 끝나지 않았다는 뜻이죠? 게임이 계속 진행되기 위해서는 두 가지 조건을 만족해야 합니다.
#
# 아직 사용자가 정답을 맞히지 않았다.
# 아직 사용자에게 기회가 남았다.
# 사용자가 입력한 값은 변수 guess에 저장되어 있고, 사용자 시도 횟수는 변수 tries에 저장되어 있다고 합시다. 그러면 while문의 조건 부분은 이렇게 쓸 수 있습니다.
#
#
# while guess != ANSWER and tries < NUM_TRIES:
# 그렇다면 while문 전에 두 변수에 대한 정의도 미리 필요하겠죠? guess는 처음에 임시적으로 -1로 저장하겠습니다. 그리고 tries는 0부터 시작하면 됩니다.
#
#
# guess = -1
# tries = 0
#
# while guess != ANSWER and tries < NUM_TRIES:
#     # 여기에 코드를 작성하세요
# while문의 수행 부분 틀
# while문의 수행 부분은 어떻게 쓸 수 있을까요? 수행 부분에서는 크게 세 가지를 해야 합니다.
#
# 사용자에게 입력을 받는다.
# 사용자 시도 횟수(tries)를 1 만큼 늘린다.
# 사용자가 입력한 숫자(guess)가 ANSWER보다 큰지, 작은지에 따라 상황에 맞는 동작을 한다.
# 이것을 코드로 옮기면 이렇습니다.
#
#
# while guess != ANSWER and tries < NUM_TRIES:
#     guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(NUM_TRIES - tries)))
#     tries += 1
#
#     if ANSWER > guess:
#         print("Up")
#     elif ANSWER < guess:
#         print("Down")
# while문이 끝나고 나면?
# while문에서 빠져 나오게 되면 무엇을 해야 할까요? 두 가지 시나리오가 있는데요.
#
# 사용자가 정답을 맞혀서 빠져나온 경우
# 사용자가 정답은 못 맞혔지만, 기회를 다 사용해서 빠져나온 경우
# 각 상황에 맞는 내용이 출력되도록 코드를 작성하면 이렇습니다.
#
#
# if guess == ANSWER:
#     print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
# else:
#     print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))
# 모범 답안
# import random
#
# # 상수 정의
# ANSWER = random.randint(1, 20)
# NUM_TRIES = 4
#
# # 변수 정의
# guess = -1
# tries = 0
#
# while guess != ANSWER and tries < NUM_TRIES:
#     guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(NUM_TRIES - tries)))
#     tries += 1
#
#     if ANSWER > guess:
#         print("Up")
#     elif ANSWER < guess:
#         print("Down")
#
# if guess == ANSWER:
#     print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
# else:
#     print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))