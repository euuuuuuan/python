# 상수 (constant)
# 상수는 변수명을 대문자로 작성한다. 일종의 약속.
# 1. 코드를 보는 입장에서 상수와 일반 변수를 구분짓기 위함이다.
# 2. 실수를 하지 않기 위함이다.

PI = 3.14 # 원주율 '파이'

# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
print(f"반지름이 {radius}면, 넓이는 {calculate_area(radius)}")

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
