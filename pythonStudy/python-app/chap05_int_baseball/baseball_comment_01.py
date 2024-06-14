# 실습 설명
# 숫자 야구 게임을 한 단계씩 완성해 나갑시다. 먼저 정답 숫자 3개를 뽑아 주는 generate_numbers() 함수를 작성할 것입니다. 이 함수는 무작위로 0과 9 사이의 서로 다른 숫자 3개를 뽑고, 그 숫자들이 담긴 리스트를 리턴합니다.
#
# 실습 결과
#
# print(generate_numbers())
#
# [5, 9, 2]
# 각 숫자는 매번 다르겠죠? 서로 다른 3개의 숫자가 나오면 됩니다.
#
# 셀프 채점
# 다음 항목들이 제대로 구현되었는지 확인해 보세요!
#
# 실행할 때마다 3개의 서로 다른 숫자가 리스트에 들어간다.
#
#
# 리스트에는 0부터 9까지의 숫자들만 들어있다.
#
#
# 힌트2/2
#
# 해설 보기
#
# 해설
# 0과 9 사이의 숫자 3개를 무작위로 뽑아야 하는데요. 숫자 야구 게임에서는 숫자의 '순서'도 중요합니다. 여러 값을 순서에 맞게 보관해야 하니까, 리스트를 사용하면 되겠죠? 그럼 먼저 빈 리스트를 만드는 것부터 시작합시다.
#
#
# numbers = []
# 우리는 총 3개의 숫자를 추가하고 싶은 거니까, numbers 리스트에 값이 3개 미만인 동안 반복문을 돌겠습니다.
#
#
# while len(numbers) < 3:
# 그리고 while문의 수행 부분에서 리스트에 숫자를 추가하면 되는데요. 숫자를 무작위로 뽑는 건 randint() 함수를 사용해서 할 수 있겠죠?
#
#
# while len(numbers) < 3:
#     new_number = randint(0, 9)
# 이제 여기서 조금 주의하셔야 할 게 있습니다. 이 new_number를 무작정 추가하면, 리스트에 중복값이 들어갈 수도 있습니다. new_number가 numbers 리스트에 없는 경우에만 추가해야겠죠?
#
#
# while len(numbers) < 3:
#     new_number = randint(0, 9)
#     if new_number not in numbers:
#         numbers.append(new_number)
# 반복문에서 나오면 numbers를 리턴하기만 하면 됩니다.
#
#
# return numbers
# 모범 답안
#
# from random import randint
#
#
# def generate_numbers():
#     numbers = []
#
#     while len(numbers) < 3:
#         num = randint(0, 9)
#         if num not in numbers:
#             numbers.append(num)
#
#     print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
#     return numbers
#
#
# # 테스트 코드
# print(generate_numbers())