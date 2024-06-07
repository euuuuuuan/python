numbers = []
numbers.append(5) # 리스트 안에 인덱스를 추가한다. (추가 연산)
numbers.append(8)
print(len(numbers)) # len은 리스트의 길이값을 나타내준다.
print(numbers)

numbers1 = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers1[3] # 인덱스 삭제 -> 삭제된 위치에 뒤 인덱스들을 땡겨온다.
print(numbers1)
numbers1.insert(4, 37)
# 해당 인덱스 위치에 인덱스 값을 삽입한다. (삽입 연산)
# 삽입된 위치에 있던 인덱스부터 뒤의 인덱스들은 오른(뒤)쪽으로 밀려난다.
print(numbers1)
