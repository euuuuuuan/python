def hello():  # 함수 정의의 첫줄 : 헤더
    print("Hello!")
    print("Welcome to My World!")


#    hello() # 탭을 하면 hello 함수의 내용으로 인식하기 때문에 탭을 지운다.
hello()
hello()
hello()


# 커피 레시피 예제 실습
def cafe_mocha_recipe():
    print("1. 준비된 컵에 초코 소스를 넣는다.")
    print("2. 에스프레소를 추출하고 잔에 부어 준다.")
    print("3. 초코 소스와 커피를 잘 섞어 준다.")
    print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("5. 생크림을 얹어 준다.")
    print("1. 준비된 컵에 초코 소스를 넣는다.")
    print("2. 에스프레소를 추출하고 잔에 부어 준다.")
    print("3. 초코 소스와 커피를 잘 섞어 준다.")
    print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("5. 생크림을 얹어 준다.")

cafe_mocha_recipe()

def hello(name):
    print("Hello!")
    print(name)
    print("Welcome")

hello("Chris") # 파라미터 parameter
hello("Michael")

# 여러개의 파라미터는 어떻게 할까?
# 함수(Function)
def print_sum(a, b, c):
    print(a + b + c)


print_sum(7, 3, 2)

# 세 수의 곱을 알려주는 프로그램을 만들려고 합니다.

# 파라미터로 정수 값 세 개를 받고, 세 수의 곱을 출력하는 함수
# multiply_three_numbers를 만들어 보세요.
def multiply_three_numbers(num_1, num_2, num_3):
    print(num_1 * num_2 * num_3)

multiply_three_numbers(10, 6, 4)
multiply_three_numbers(5, 1, 3)

# return
def get_square(x):
    return x * x

y = get_square(3)
print(y) # 9
print(get_square(3) + get_square(4)) # 25



