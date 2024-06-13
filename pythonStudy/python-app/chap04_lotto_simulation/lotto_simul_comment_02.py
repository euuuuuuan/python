# 실습 설명
# main.py 파일의 draw_winning_numbers() 함수를 작성하세요. 이 함수는 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다. 앞서 정의한 generate_numbers() 함수를 잘 활용하면, 함수를 간결하게 작성할 수 있습니다.
#
# 실습 결과
#
# print(draw_winning_numbers())
#
# [4, 12, 14, 28, 40, 41, 6]
# 각 숫자는 매번 다르겠죠? 정렬된 6개의 숫자와 1개의 보너스 번호가 나오면 됩니다.

# 나의 문제 해결
from random import randint
import random

def generate_numbers(n):
    return random.sample(range(1, 45), n)

def draw_winning_numbers():
    plus_numbers = generate_numbers(6)
    plus_numbers.sort()
    plus_numbers.append(random.sample(range(1, 45), 1)[0])
    return plus_numbers

# 테스트 코드
print(draw_winning_numbers())

# 셀프 채점
# 다음 항목들이 제대로 구현되었는지 확인해 보세요!
#
# 실행할 때마다 7개의 서로 다른 숫자가 리스트에 들어간다.
#
#
# 리스트의 첫 6개 값만 정렬되어 있고, 마지막 보너스 번호는 정렬되어 있지 않다.

# 해설
# 우선 일반 번호 7개를 뽑을게요. 이건 그냥 generate_numbers() 함수를 사용하면 되겠죠?
#
#
# winning_numbers = generate_numbers(7)
# 7개의 요소 중, 첫 6개는 일반 당첨 번호고 마지막 1개는 보너스 번호입니다. 그러면 첫 6개만 정렬하면 되겠죠?
#
# 첫 6개만 정렬하는 방식은 여러 가지가 있을 텐데요. 그 중 한 가지 방법만 보여 드릴게요.
#
# 리스트 슬라이싱을 이용해서, 일반 당첨 번호(첫 6개)와 보너스 번호(마지막 1개)를 분리한다.
# sorted() 함수를 사용해서 일반 당첨 번호만 정렬한다.
# 일반 당첨 번호와 보너스 번호를 다시 합친다.
# 이걸 코드로 옮기면 이렇게 됩니다.
#
#
# winning_numbers = generate_numbers(7)
# return sorted(winning_numbers[:6]) + winning_numbers[6:]
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
# def draw_winning_numbers():
#     winning_numbers = generate_numbers(7)
#     return sorted(winning_numbers[:6]) + winning_numbers[6:]
#
# # 테스트 코드
# print(draw_winning_numbers())
