# 코멘트 (주석)

print("hello world") # 이것도 코멘트

# 추상화
# 1. 변수 (Variable) 2. 함수(Function) 3. 객체(Object)
# 변수
# 값을 저장하는 것
# x = 254 y 317
# print (x + y)
# 추상화의 목적 : 복잡한 디테일 숨기기.

# 함수
# 명령들을 저장하는 것
# print 함수
# 내부적인 기능을 몰라도 출력문임을 알고 쓸 수 있다.

burger_price = 4990 # '=' 등호는 지정연산자로서 오른쪽 값이 왼쪽으로 넘어가는 것을 의미
fries_price = 1490
drink_price = 1250

print(burger_price)
print(burger_price * 2)
print(burger_price + fries_price)
print(burger_price * 3 + fries_price * 2 + drink_price * 5)

def hello(): # 함수 정의의 첫줄 : 헤더
    print("Hello!")
    print("Welcome to myWorld!")

    hello()

