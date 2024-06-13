# 리스트 (programing-data)
numbers = [2, 3, 5, 7, 11, 13] # 괄호 안의 내용은 요소라고 한다.
names = ["윤수", "혜린", "태호", "영훈"]

print(numbers)
print(names)

# 인덱싱 (indexing)
print(names[1]) # 배열은 0번부터 시작한다.
print(numbers[1] + numbers[3])

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)

print(numbers[-1])
print(numbers[-2])

# print(numbers[-7])
# print(numbers[6])
# 위 두가지는 리스트 범위를 벗어나기 때문에 오류가 발생한다.

# 리스트 슬라이싱 (programing-data slicing)
print(numbers[0:4]) # 배열 0부터 3번까지 출력
print(numbers[2:]) # 배열 인덱스 2부터 출력
print(numbers[:3]) # 처음부터 인덱스 3까지 출력

new_list = numbers[:3] # [2, 3, 5]
print(new_list[2])
numbers[0] = 7 # 0 번 인덱스에 7이라는 값을 덮어씌운다.
print(numbers)

numbers[0] = numbers[0] + numbers[1]
print(numbers[0])
print(numbers)



