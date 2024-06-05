name = "김현승"
x = 7
x = x + 1


# = 등호는 지정연산자 assignment operator 라고 한다.
# 오른쪽의 연산 후에 등호 왼쪽 부분의 변수에 저장하는 것이다.

def hello():
    print("Hello!")
    print("Welcome to hell!")


print("함수 호출 전")
hello()
print("함수 호출 후")
print()


def square(x):
    return x * x


print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

print()


# 리턴문을 값 돌려주기 / 함수 즉시 종료하기
def square(x):
    print("함수 시작 전")
    return x * x
    print("함수 시작 후")


print(square(3))
print("Hello World")


# square 함수 안의 함수 시작 후 출력은 안된다.


def print_squre(x):
    print(x * x)


def get_square(x):
    return x * x


print_squre(3)  # print문은 함수 안에 print문으로 출력되어 나오고
get_square(3)  # get문은 함수안에 return문으로 값만 가져나오기 때문에
# 따로 출력문이 없을 경우 값을 출력하지 못한다.

print(get_square(3))

print(print_squre(3))  # None 출력


# 파이썬에서 return문이 따로 없으면
# return 값이 없다는 의미에서 None이 출력된다.

# 반환할 값을 명시했을 때
def return_message():
    return "안녕하세요"


return_message()


# 반환할 값을 명시할 때 return 문을 사용해요.
# 위 코드에서는 return_message() 함수를 호출하면 반환하도록
# 명시한 "안녕하세요"라는 문자열을 함수를 호출한 자리로 돌려줘요.

# 반환할 값을 명시하지 않았을 때
def return_nothing():
    message = "안녕하세요"


return_nothing()


# 위 코드에는 값을 반환하기 위한 return 문이 없어요.
# 이런 경우 None 을 함수를 호출한 자리로 돌려줘요.

def return_nothing():
    return


return_nothing()
# 위 코드는 어떨까요? return 문이 쓰였지만 반환할 값이 명시되어 있지 않아요.
# 이때에도 None 을 반환해요.

# “반환하다” VS “출력하다”
# return 과 print 차이를 이해하기 위해서는 각각의 역할을 정확히 이해해야 해요.
# return 문은 값을 호출한 자리에 반환해줘요
# print 함수는 주어진 인수를 출력해줘요.

# 1 def return_message():
# 2    return "안녕하세요"
# 3
# 4
# 5 return_message()
# 파이썬 인터프리터[1]가 코드를 위에서부터 아래로 해석해요.
# 하지만 1번째 줄에서는 함수 정의만 이루어지고, return "안녕하세요" 코드 실행은
# 5번째 줄의 return_message()에 의해 이루어져요.
# return_message() 함수를 호출하면 정의한 return_message 함수를 찾아
# 함수 본문을 실행하는 거예요.
# 그래서  return "안녕하세요" 실행 결과로 "안녕하세요"라는
# 문자열을 호출한 자리에 반환해요
# 즉, 아래와 같다고 생각하시면 돼요.
# 5 "안녕하세요"
# 그런데 "안녕하세요" 문자열을 직접 확인할 수는 없어요.
# 반환을 했을 뿐 출력을 하지 않았기 때문이에요.