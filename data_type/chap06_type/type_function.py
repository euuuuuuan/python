# 어떠한 자료형인지 알아내는 type 명령어

print(type(3)) # int
print(type(3.0)) # float
print(type("3")) # str

print()

print(type("True")) # str
print(type(True)) # bool

print()

def hello():
    print("Hello world!")
print(type(hello)) # 위에서 정의한 hello함수도 자료형으로 구분한다.
# 따라서 function 출력

print(type(print))
# builtin_function_or_method
# 파이썬 기본 내장함수 출력