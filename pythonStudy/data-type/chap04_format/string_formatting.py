# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
# str 형변환을 일일이 해줘야 하는 번거로움을 해결하고 싶다.
# 문자열 formatting 기법을 사용하자.

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

# 다음날을 출력하고 싶으면?
print(date_string.format(year, month, day + 1))

print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

# 위의 순서를 바꾸고 싶으면? 파라미터 순서를 바꾸는 것도 있다.
# 하지만 다른 방법을 써보자. 아래 코드를 참고하자.
print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))

print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))
# f는 소수형 floating point 약자
# 앞에 .2는 소수점 둘째자리까지 반올림하는 명령어
# 정수형으로 하고 싶으면 .0을 하면 된다.

# %기호
name = "최지웅"
age = 32
print("제 이름은 %s이고 %d살입니다." % (name, age))
# 이제는 잘 쓰지 않는 오래된 방식입니다.
# %s, %d와 같은 '포맷 스트링'이라는 것을 사용하는데요.
# C나 자바 등 많은 언어들에서 이와 유사한 방식으로 문자열을 포매팅합니다.

# format() 메소드
name = "최지웅"
age = 32
print("제 이름은 {}이고 {}살입니다.".format(name, age))


# f-string
name = "최지웅"
age = 32
print(f"제 이름은 {name}이고 {age}살입니다.")
# 파이썬 3.6에서 추가된 문법인데요.
# 훨씬 편리하기 때문에 최근에 많이 사용하는 방식입니다.


# 우측 실행기에 제공된 코드에서 wage는
# 1시간에 얼마 버는지를 나타내는 값이고,
# exchange_rate는 1달러를 한국 돈으로 바꾸면 얼마인지
# 나타내는 값(환율)입니다.
# 1시간 동안 번 금액은 wage * 1의 결괏값인 5달러이고,
# 이 금액을 한국 돈으로 환전하면 wage * 1 * exchange_rate의
# 결괏값인 5710.8원이 됩니다.
#
# 이번 토픽에서 배운 문자열 포매팅을 활용해서
# 아래의 문장들을 출력하세요.

# 1시간에 5달러 벌었습니다.
# 5시간에 25달러 벌었습니다.
# 1시간에 5710.8원 벌었습니다.
# 5시간에 28554.0원 벌었습니다.

# 주어진 변수(wage, exchange_rate)와 문자열 포매팅을 반드시 이용하셔야 합니다.
# 그리고 원화 금액은 소수점 첫째 자리까지만 출력되어야 합니다.

wage = 5
time1 = 1
time2 = 5
exchange_rate = 1142.16
krw = wage * 1 * exchange_rate
print(f"{time1}시간에 {wage * time1}달러 벌었습니다.")
print(f"{time2}시간에 {wage * time2}달러 벌었습니다.")
print(f"{time1}시간에 {krw * time1:.1f}달러 벌었습니다.")
print(f"{time2}시간에 {krw * time2:.1f}달러 벌었습니다.")


# 5시간에 25달러 벌었습니다.를 출력해야 합니다. 5시간을 일했으니, 수입은 wage * 5로 표현할 수 있겠죠? 그리고 단위는 달러입니다.
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))

# 1시간에 5710.8원 벌었습니다.를 출력해야 합니다. 1시간 수입을 달러로 표현하면 그냥 wage * 1인데요. 한국 원화로 변환해야 하기 때문에 wage * 1 * exchange_rate으로 표현할 수 있습니다.
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))

# 그리고 소수점 첫째 자리까지만 출력하기 위해서 이렇게 하면 됩니다.
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))

# 5시간에 28554.0원 벌었습니다.를 출력해야 합니다. 5시간 수입을 달러로 표현하면 wage * 5인데요. 한국 원화로 변환해야 하기 때문에 wage * 5 * exchange_rate으로 표현할 수 있습니다.
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))
