def my_function():
    x = 3
    print(x)

my_function()
print()
# print(x) // 함수 내에서 정의된 변수는 local vraible 로컬 변수라고 한다.
# 그러므로 변수 x의 스코프(유효 범위) my_function 내부인 것이다.

x = 2 # 함수 밖에서 정의한 함수는 global variable 글로벌 변수라고 한다.
def my_function():
    print(x)

my_function()
print()


x = 2
def my_function():
    x = 3
    print(x)

my_function() # 3
print() # 2

# 파라미터도 로컬 변수다.
def square(x):
    return x * x

print(square(3))

# scope
# 변수가 사용 가능한 범위
# 로컬 변수 : 변수를 정의한 함수 내에서만 사용가능
# 글로벌 변수 : 모든 곳에서 사용 가능
# 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고나서
# 글로벌 변수를 찾는다.