# 실습 설명
# 이제 스트라이크 수와 볼 수를 알려 주는 get_score() 함수를 작성할 것입니다. 이 함수는 두 개의 파라미터를 받는데요.
#
# guesses: 유저가 뽑은 번호 3개가 담긴 리스트
# solution: 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트
# 두 리스트를 비교해서 스트라이크와 볼의 개수를 계산하고 리턴합니다. 여기서 새로운 개념을 알려 드릴게요. 파이썬의 함수에서 여러 값을 리턴하고 싶으면 이렇게 할 수 있습니다.
#
#
# def square_and_cube(x):
#     square = x ** 2
#     cube = x ** 3
#     return square, cube
# 또한 여러 리턴 값을 한 번에 여러 변수에 저장할 수도 있습니다. 아래와 같이 코드를 작성하면 square_and_cube(2)의 첫 번째 리턴 값이 변수 s에 저장되고, 두 번째 리턴 값이 변수 c에 저장됩니다.
#
#
# s, c = square_and_cube(2)
# print(s)
# print(c)
#
# 4
# 8
# 이런 식으로 get_score() 함수는 스트라이크와 볼의 개수를 모두 리턴하도록 해야 합니다. 예를 들어서 아래 코드를 실행해 볼게요.
#
#
# s, b = get_score([2, 7, 4], [2, 4, 7])
# print(s)  # 스트라이크 수 출력
# print(b)  # 볼 수 출력
# 2는 숫자의 값과 위치가 모두 일치하기 때문에 스트라이크입니다. 그리고 7과 4의 경우, 숫자의 값은 일치하지만 위치가 틀렸기 때문에 볼입니다. 스트라이크 1개와 볼 2개니까, 정수 1과 2를 모두 리턴해야 하는 거죠. 그러면 리턴된 값이 각각 변수 s와 b에 지정되어, 아래처럼 출력됩니다.
#
#
# 1
# 2
# 실습 결과
# get_score() 함수를 완성하고 아래 # 테스트 코드를 실행한 결과는 다음과 같습니다.
#
#
# # 테스트 코드
# s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
# print(s_1, b_1)
#
# s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
# print(s_2, b_2)
#
# s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
# print(s_3, b_3)
#
# s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
# print(s_4, b_4)
#
# 1 2
# 0 3
# 2 0
# 3 0

# 해설
# 리스트 guesses와 리스트 solution이 있습니다. 스트라이크와 볼을 판단하는 방법을 각각 살펴봅시다.
#
# 스트라이크 판단 방법
# guesses의 인덱스 i에 있는 숫자와 solution의 인덱스 i에 있는 숫자가 동일하면 스트라이크입니다. 이렇게 작성할 수 있겠죠?
#
#
# for i in range(3):
#     if guesses[i] == solution[i]:
#         strike_count += 1
# 볼 판단 방법
# guesses의 인덱스 i에 있는 숫자가 '볼'이기 위해서는 이 두 가지 조건을 충족해야 합니다.
#
# 이 숫자가 solution 안에도 있어야 한다.
# 이 숫자가 solution의 인덱스 i에 있으면 안 된다.
# 그러면 코드를 이렇게 작성할 수 있습니다.
#
#
# for i in range(3):
#     if guesses[i] in solution and guesses[i] != solution[i]:
#         ball_count += 1
# 두 가지 코드 합치기
# 스트라이크를 판단하는 코드와 볼을 판단하는 코드를 합쳐 봅시다.
#
#
# for i in range(3):
#     if guesses[i] == solution[i]:
#         strike_count += 1
#
# for i in range(3):
#     if guesses[i] in solution and guesses[i] != solution[i]:
#         ball_count += 1
# 이렇게 해도 되지만, 반복문을 한 번만 돌면 더 효율적이겠죠?
#
#
# for i in range(3):
#     if guesses[i] == solution[i]:
#         strike_count += 1
#     if guesses[i] in solution and guesses[i] != solution[i]:
#         ball_count += 1
# 심지어 이것보다 더 깔끔하게 작성할 수도 있습니다. if문의 조건 부분을 통과하지 못했다는 것은 어떤 의미일까요? guesses의 인덱스 i 값이 solution의 인덱스 i 값과 다르다는 뜻이겠죠? 그러면 elif문을 사용해서 조건 부분을 아래 코드처럼 단순화할 수 있습니다.
#
#
# for i in range(3):
#     if guesses[i] == solution[i]:
#         strike_count += 1
#     elif guesses[i] in solution:
#         ball_count += 1
# 모범 답안
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
# # 테스트 코드
# s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
# print(s_1, b_1)
#
# s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
# print(s_2, b_2)
#
# s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
# print(s_3, b_3)
#
# s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
# print(s_4, b_4)