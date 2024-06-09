
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    # read의 약자 r, write의 약자 w
    # as f라는 변수에 저장
    for line in f:
        # print(line)
        print(line.strip())  # strip을 붙이게 되면 띄어쓰기가 사라진다.
    # 읽어들인 파일을 f라는 타입에 저장한다.
    # 불러온 파일의 출력 결과가 한줄씩 띄어서 나온다.
    # 파일 안에서 enter로 줄바꿈을 했는데 이것은 파이썬에서 \n으로 인식하기 때문이다.

# ex)
print("Hello")
print("Hello")  # 출력시 기본적으로 한줄 띈(enter) 결과가 나온다.
print("Hello\n")
print("Hello")

# strip
print("         abd     def           ".strip())  # 앞 뒤의 화이트 스페이스 제거
print("   \t       \n      abd     def     \n\n\n      ".strip())  # 앞 뒤의 화이트 스페이스 제거


# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))
full_name = "Kim, Yuna"
print(full_name.split(","))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(last_name, first_name)

print("   \t       \n      2     3     \n 5 7 11\n\n      ".split())
numbers = "   \t       \n      2     3     \n 5 7 11\n\n      ".split()
print(numbers[0] + numbers[1]) # 23이 출력된 것은 split은 문자열임을 알 수 있다.







