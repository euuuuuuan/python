# if문과 else 문
# if 조건 부분:
    # 수행 부분
# else:
    # 수행 부분

temperature = 16
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")

# if 온도가 10도 이하다:
    # 자켓을 입는다.
# else:
    # if 온도가 15도 이하다:
        # 긴팔을 입는다.
    # else:
        # 반팔을 입는다.

# 대학 성적을 매길때
# if 점수가 90점 이상이다:
    # A를 준다
# else:
    # if 점수가 80점 이상이다:
        # B를 준다
    # else:
        # if 점수가 70점 이상이다:
            # C를 준다
        # else:
            # if 점수가 60점 이상이다:
                # D를 준다
                # else:
                    # F를 준다
# 위는 코드가 지저분해 보이고
# 들여쓰기가 많아 가독성이 떨어진다.

# 이럴때 elif문이란 것을 활용하면 된다.
# 아래 코드를 참고하자.

# if 점수가 90점 이상이다:
    # A를 준다
# elif 점수가 80점 이상이다:
    # B를 준다
# elif 점수가 70점 이상이다:
    # C를 준다
# elif 점수가 60점 이상이다:
    # D를 준다
# else:
    # F를 준다

# 실습 설명
# 학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.
#
# 이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요.
# 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다.
# 규칙은 다음과 같습니다.
#
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만
# print_grade() 함수는 파라미터로 중간고사 점수 midterm_score와
# 기말고사 점수 final_score를 받아서 최종 성적을 출력합니다.

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 여기에 코드를 작성하세요
    if total >= 90:
        print("A")
    elif 80 <= total < 90:
        print("B")
    elif 70 <= total < 80:
        print("C")
    elif 60 <= total < 70:
        print("D")
    elif total < 60:
        print("F")


# 테스트 코드
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

# 모범 답안
# def print_grade(midterm_score, final_score):
#     total = midterm_score + final_score
#     if total >= 90:
#         print("A")
#     elif total >= 80:
#         print("B")
#     elif total >= 70:
#         print("C")
#     elif total >= 60:
#         print("D")
#     else:
#         print("F")