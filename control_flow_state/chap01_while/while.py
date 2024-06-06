# while
# while 조건 부분:
# 수행 부분 (들여쓰기 필수)

i = 1
while i <= 3:
    print("I'm handsome!")
    i += 1

print()

i = 0
while i < 3:
    print("I'm good!")
    i += 1

# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력해 보세요.
i = 0
while i < 100:
    i += 3 - 1
    print(i)

    # 모범 답안
# i = 1
# while i <= 50:
#     print(i * 2)
#     i += 1