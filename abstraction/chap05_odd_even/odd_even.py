# 어떤 수가 짝수인지 홀수인지 판단하는 is_evenly_divisible() 함수를 작성하세요.
# 이 함수는 number(숫자)를 파라미터로 받습니다.
# 짝수인 경우, 즉 number가 2로 나누어떨어질 경우에는 True를 리턴합니다.
# 홀수인 경우, 즉 number가 2로 나누어떨어지지 않을 경우에는 False를 리턴합니다.
#
# 함수 안에는 print() 함수가 아닌, return문을 사용해야 합니다.
# 참고로 불린 개념을 잘 사용하면, 함수를 단 한 줄로 작성할 수 있습니다.

def is_evenly_divisible(number):
    return number % 2 == 0


# 테스트 코드
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))

# 실습 결과
# False
# False
# True
# True
# False