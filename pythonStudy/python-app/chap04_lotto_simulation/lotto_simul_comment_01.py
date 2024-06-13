# 실습 설명
# 로또 시뮬레이션 프로그램을 한 단계씩 완성해 나갑시다.
#
# 먼저 main.py 파일의 generate_numbers() 함수를 작성하세요. 이 함수는 파라미터로 정수 n을 받습니다. 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다. 참고로 이 함수는 참가자의 번호를 뽑는 데에도 쓰이고, 보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.
# 나의 문제 해결
from random import randint
import random
def generate_numbers(n):
    return random.sample(range(1, 45), n)

print(generate_numbers(6))

# 실습 결과
#
# print(generate_numbers(6))
#
# [16, 2, 30, 40, 15, 33]

# 셀프 채점
# 다음 항목들이 제대로 구현되었는지 확인해 보세요!
#
# 실행할 때마다 n개의 서로 다른 숫자가 리스트에 들어간다.
#
#
# 리스트의 값들이 정렬되어 있지 않다.

# 해설
# 1과 45 사이의 번호 n개를 무작위로 뽑아야 하는데요. 우선 빈 리스트를 만드는 것부터 시작합시다.
#
#
# numbers = []
# 우리는 총 n개의 번호를 추가하고 싶은 거니까, numbers 리스트에 값이 n개 미만인 동안 반복문을 돌겠습니다.
#
#
# while len(numbers) < n:
# 그리고 while문의 수행 부분에서 리스트에 번호를 추가하면 되는데요. 번호를 무작위로 뽑는 건 randint() 함수를 사용해서 할 수 있겠죠?
#
#
# while len(numbers) < n:
#     num = randint(1, 45)
# 이제 여기서 조금 주의하셔야 할 게 있습니다. 이 new_number를 무작정 추가하면, 리스트에 중복값이 들어갈 수도 있습니다. new_number가 numbers 리스트에 없는 경우에만 추가해야겠죠?
#
#
# while len(numbers) < n:
#     num = randint(1, 45)
#     if num not in numbers:
#         numbers.append(num)
# 반복문에서 나오면 numbers는 번호 n개가 들어 있을 텐데, 이제 numbers를 리턴하기만 하면 됩니다.
#
#
# return numbers
# 모범 답안
#
# from random import randint
#
#
# def generate_numbers(n):
#     numbers = []
#
#     while len(numbers) < n:
#         num = randint(1, 45)
#         if num not in numbers:
#             numbers.append(num)
#
#     return numbers
#
#
# # 테스트 코드
# print(generate_numbers(6))