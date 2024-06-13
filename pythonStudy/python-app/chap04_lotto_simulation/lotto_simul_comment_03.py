# 실습 설명
# main.py 파일의 count_matching_numbers() 함수를 작성하세요. 이 함수는 참가자가 뽑은 6개의 번호 리스트와 당첨 번호 6개의 리스트 중 몇 개의 숫자가 일치하는지 알려 주는 함수입니다. 파라미터로 리스트 numbers와 리스트 winning_numbers를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
#
# 실습 결과
# 예를 들어서 아래 코드를 실행하면,
# 두 리스트에 2, 11, 14 3개가 겹치기 때문에 3이 출력됩니다.
#
#
# print(count_matching_numbers([2, 7, 11, 14, 25, 40],
# [2, 11, 13, 14, 30, 35]))
#
# 3

# 또 아래 코드를 실행하면, 두 리스트에 14만 겹치기 때문에 1이 출력되겠죠?
#
#
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
#
# 1

# 나의 문제 해결
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count


print(count_matching_numbers([2, 7, 11, 14, 25, 40],
                             [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40],
                             [14]))
# 힌트 1
#
# 두 리스트의 번호들을 보면서 비교하면 될 텐데요. 이것을 어떤 로직으로 할 수 있을까요?
#
# 겹치는 번호 수를 세기 위한 변수 count를 정의한다. count는 당연히 0부터 시작한다.
# numbers의 각 원소를 본다.
# 해당 원소가 winning_numbers에 있는지 확인한다.
# 만약 보고 있는 numbers의 원소가 winning_numbers에도 있으면 count를 1 늘린다.
# 위의 과정을 코드로 옮기면 됩니다.

# 힌트 2
#
# 반복문을 통해 numbers의 각 원소를 볼 수 있습니다.
#
#
# for num in numbers:
# 그리고 리스트의 in 키워드를 통해 현재 보고 있는 원소인 num이 winning_numbers에 있는지 확인할 수 있습니다.
#
#
# num in winning_numbers

# 해설
# 일단 count라는 변수를 정의하고, 초깃값을 0으로 설정하겠습니다.
#
#
# count = 0
# count는 파라미터로 받은 두 리스트에서 총 몇 개의 번호가 겹치는지 세는 용도입니다. 이제 리스트의 번호들을 보면서 비교를 하면 될 텐데요. 이것을 어떤 로직으로 할 수 있을까요?
#
# numbers의 각 원소를 본다.
# 해당 원소가 winning_numbers에 있는지 확인한다.
# 만약 보고 있는 numbers의 원소가 winning_numbers에도 있으면 count를 1 늘린다.
# 위의 과정을 코드로 옮기면 됩니다. numbers의 각 원소는 반복문을 통해 볼 수 있습니다.
#
#
# for num in numbers:
# 그리고 리스트의 in 키워드를 통해 현재 보고 있는 원소인 num이 winning_numbers에 있는지 확인할 수 있습니다.
#
#
# for num in numbers:
#     if num in winning_numbers:
#         count += 1
# 반복문이 끝나면, 누적된 count 값을 리턴하면 되겠죠?
#
#
# return count
# 모범 답안
#
# def count_matching_numbers(numbers, winning_numbers):
#     count = 0
#
#     for num in numbers:
#         if num in winning_numbers:
#             count = count + 1
#
#     return count
#
#
# # 테스트 코드
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))


# 다른 풀이
# def count_matching_numbers(list_1, list_2):
#   # 코드를 작성하세요.
#
#   same_numbers = list(set(list_1).intersection(list_2))
#   return len(same_numbers)
#
# # 테스트
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))