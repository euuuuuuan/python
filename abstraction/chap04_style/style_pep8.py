# 스타일
# 버거를 주문할 시에 혜택 차원에서 음료수 및 감자튀김을 받을 수 있다.
# vs
# 버거를 주문하면 음료수와 감자튀김은 서비스다.
# 아래문장이 간결하고 의미 전달이 깔끔하다.
# 코딩에도 스타일이 존재한다.
# 이해하기 쉬운 코드 = 좋은 스타일을 가진 좋은 코드

print(6.28*4)
print(3.14*4*4)

print(6.28*8)
print(3.14*8*8)

a = 3.14
b = 4
print(2*a*b)
print(a*b*b)
b = 8
print(2*a*b)
print(a*b*b)

a = 3.14 # 원주율(파이)
b = 4 # 반지름
print(2*a*b)
print(a*b*b)
b = 8 # 반지름
print(2*a*b)
print(a*b*b)
# 하지만 a와 b가 무슨 변수인지 모른다.

pi = 3.14 # 원주율(파이)
radius = 4 # 반지름
print(2*pi*radius)
print(pi*radius*radius)
radius = 8 # 반지름
print(2*pi*radius)
print(pi*radius*radius)

PI = 3.14 # 원주율(파이)

radius = 4 # 반지름
print(2 * pi * radius)
print(pi * radius * radius)

radius = 8 # 반지름
print(2 * pi * radius)
print(pi * radius * radius)
# 띄어쓰기나 빈 줄 같은 것을
# 화이트 스페이스라고 부른다.
# 가독성을 높여준다. (보기 좋은 코드)

PI = 3.14

def calculate_circumference(r):
    return 2 * PI * r

def calculate_area(r):
    return PI * r * r

radius = 4 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

# 여기서 조금 더 설명을 추가하자면,

PI = 3.14

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

# 회사마다 각자 스타일 가이드가 존재한다.
# 파이썬에는 스타일 가이드가 있다.
# PEP8 스타일 가이드 ( https://peps.python.org/pep-0008/)
# 가장 중요한 부분

## 이름 ---------------------------------------------------------
# 이름 규칙 ---------------------------------------------------------
# 모든 변수와 함수 이름은 소문자로 쓰고, 여러 단어일 경우 _로 나눠주세요.
# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good
some_variable_name = 1

def some_function_name():
    print("Hello")

# 모든 상수 이름은 대문자로 쓰고, 여러 단어일 경우 _로 나눠주세요.
# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14

# 의미 있는 이름(변수)
# bad (의미 없는 이름)
a = 2
b = 3.14
print(b * a * a)

# good (의미 있는 이름)
radius = 2
PI = 3.14
print(PI * radius * radius)

# 의미 있는 이름(함수)
# bad (의미 없는 이름)
def do_something():
    print("Hello, world!")

# good (의미 있는 이름)
def say_hello():
    print("Hello, world!")

## 화이트 스페이스 ---------------------------------------------------------
# 들여쓰기 ---------------------------------------------------------
# 들여쓰기는 무조건 스페이스 4개를 사용하세요.
# bad (스페이스 2개)
def do_something():
    print("Hello, world!")

# bad (스페이스 8개)
i = 0
while i < 10:
    print(i)

# good (스페이스 4개)
def say_hello():
    print("Hello, world!")

# 함수 정의 ---------------------------------------------------------
# 함수 정의 위아래로 빈 줄이 두 개씩 있어야 합니다.
# 하지만 파일의 첫 줄이 함수 정의인 경우 해당 함수 위에는 빈 줄이 없어도 됩니다.
# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')

# good
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')

# 괄호 안 ---------------------------------------------------------
# 괄호 바로 안에는 띄어쓰기를 하지 마세요.
# bad
# spam( ham[ 1 ], { eggs: 2 } )

# good
# spam(ham[1], {eggs: 2})

# 함수 괄호 ---------------------------------------------------------
# 함수를 정의하거나 호출할 때, 함수 이름과 괄호 사이에 띄어쓰기를 하지 마세요.
# bad
def spam (x):
    print (x + 2)


spam (1)

# good
def spam(x):
    print(x + 2)


spam(1)

# 쉼표 ---------------------------------------------------------
# 쉼표 앞에는 띄어쓰기를 하지 마세요.
# bad
# print(x , y)

# good
# print(x, y)

# 지정 연산자 ---------------------------------------------------------
# 지정 연산자 앞뒤로 띄어쓰기를 하나씩 넣어 주세요.
# bad
x=1
x    = 1

# good
x = 1

# 연산자 ---------------------------------------------------------
# 기본적으로는 연산자 앞뒤로 띄어쓰기를 하나씩 합니다.
# bad
# i=i+1
# submitted +=1

# good
# i = i + 1
# submitted += 1

# 하지만 연산의 '우선 순위'를 강조하기 위해서는,
# 연산자 앞뒤로 띄어쓰기를 붙이는 것을 권장합니다.

# bad
# x = x * 2 - 1
# hypot2 = x * x + y * y
# c = (a + b) * (a - b)

# good
# x = x*2 - 1
# hypot2 = x*x + y*y
# c = (a+b) * (a-b)

# 코멘트 ---------------------------------------------------------
# 일반 코드와 같은 줄에 코멘트를 쓸 경우,
# 코멘트 앞에 띄어쓰기 최소 두 개를 입력해 주세요.
# bad
x = x + 1# 코멘트

# good
x = x + 1  # 코멘트