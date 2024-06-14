# alias (가명)
x = 5
y = x
y = 3
print(x) # 5
print(y) # 3

x = [2, 3, 5, 7, 11] # 리스트
y = x
y[2] = 4
print(x) # 2, 3, 4, 7, 11
print(y) # 2, 3, 4, 7, 11
# 파이썬에서 어떤 값을 변수에 저장하면 이름표를 부여하는 것 (주소값 개념)
# 한 이름표는 한 곳에만 달릴 수 있다.

x = [2, 3, 5, 7, 11]
y = list(x) # 리스트 복사
y[2] = 4
print(x)
print(y)