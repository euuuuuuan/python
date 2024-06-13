# 실습 설명
# main.py 파일의 check() 함수를 작성하세요. 참고로 당첨 액수는 아래 규칙에 따라 결정됩니다.
#
# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원
# check() 함수는 참가자의 당첨 금액을 리턴합니다. 파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요. numbers는 당연히 번호 6개를 담고 있고, winning_numbers는 보너스 번호까지 해서 7개를 담고 있겠죠?
#
# 실습 결과
# 예시 1
# 예를 들어서 아래 코드를 실행해 볼게요.
#
#
# numbers_test = [2, 4, 11, 14, 25, 40]
# winning_numbers_test = [4, 12, 14, 28, 40, 41, 6]
#
# print(check(numbers_test, winning_numbers_test))
# 4, 14, 40, 이렇게 번호 3개가 겹치기 때문에 5천 원에 당첨됩니다.
#
#
# 5000
# 예시 2
# 그리고 아래 코드를 실행해 볼게요.
#
#
# numbers_test = [2, 4, 11, 14, 25, 40]
# winning_numbers_test = [2, 4, 10, 11, 14, 40, 25]
#
# print(check(numbers_test, winning_numbers_test))
# 일반 번호 2, 4, 11, 14, 40, 이렇게 5개가 겹칩니다. 그리고 보너스 번호 25도 겹치죠? 그러면 5천만 원에 당첨됩니다.
#
#
# 50000000

# 나의 문제 해결
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 100000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

print(check([2, 4, 11, 14, 25, 40],
            [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40],
            [2, 4, 10, 11, 14, 40, 25]))


# 힌트 1
#
# 당첨금을 알기 위해서는 두 가지를 봐야 합니다.
#
# 참가자 번호 6개와 일반 당첨 번호 6개 중 몇 개가 일치하는지
# 참가자 번호 6개와 보너스 번호 1개 중 몇 개가 일치하는지

# 힌트 2
#
# 힌트 1의 두 가지를 코드로 나타내면 이렇습니다.
#
#
# count = count_matching_numbers(numbers, winning_numbers[:6])
# bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
# 이해되시나요? winning_numbers의 첫 6개는 일반 당첨 번호고 마지막 1개 번호는 보너스 번호이기 때문에, 이렇게 쓸 수 있습니다.

# 힌트 3
#
# 이제 count와 bonus_count에 따른 당첨금을 구해서 리턴하면 됩니다.
# 다양한 경우를 봐야 하기 때문에 if, elif, else의 조합으로 작성하셔야 합니다.

# 해설
# 일치하는 번호 개수 세기
# 당첨금을 알기 위해서는 두 가지를 봐야 합니다.
#
# 참가자 번호 6개와 일반 당첨 번호 6개 중 몇 개가 일치하는지
# 참가자 번호 6개와 보너스 번호 1개 중 몇 개가 일치하는지
# 각각을 코드로 나타내면 이렇습니다.
#
#
# count = count_matching_numbers(numbers, winning_numbers[:6])
# bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
# 이해되시나요? winning_numbers의 첫 6개는 일반 당첨 번호고 마지막 1개 번호는 보너스 번호이기 때문에, 이렇게 쓸 수 있습니다.
#
# 당첨금 리턴하기
# 이제 count와 bonus_count에 따른 당첨금을 구해서 리턴하면 됩니다. 다양한 경우를 봐야 하기 때문에 if, elif, else의 조합으로 작성하겠습니다.
#
#
# if count == 6:
#     return 1000000000
# elif count == 5 and bonus_count == 1:
#     return 50000000
# elif count == 5:
#     return 1000000
# elif count == 4:
#     return 50000
# elif count == 3:
#     return 5000
# else:
#     return 0
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
# def check(numbers, winning_numbers):
#     count = count_matching_numbers(numbers, winning_numbers[:6])
#     bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
#
#     if count == 6: