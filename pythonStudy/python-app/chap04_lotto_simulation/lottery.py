# 이제 필요한 함수를 모두 작성했습니다. 만약 모든 함수가 올바르게 동작한다면 사실상 프로젝트 완성인데요. lottery.py 라는 새로운 파일을 만든 후 여러분이 그동안 과제에서 작성한 4개의 함수들을 파일에 '복사 후 붙여넣기' 해주세요. 우리는 이 파일을 '모듈'로써 활용할 것입니다.
#
# 그리고 이 lottery_driver.py 파일을 받아 주세요. 이 파이썬 코드는 lottery.py 모듈에 있는 함수들을 사용해서 로또 100장을 시뮬레이션하고, lottery.html이라는 파일을 생성하는 역할을 합니다. 올바르게 html 파일이 생성되기 위해 아래 절차대로 진행해 주세요.
#
# 작성하신 함수들이 포함된 파일명이 lottery.py 가 맞는지 확인해 주세요. 다르다면 동일한 파일명으로 변경해 주세요.
#
# 과제 진행 중 함수명을 변경하셨다면 아래 모듈 구조를 참고하여 함수명을 변경해 주세요.
#
# lottery.py
#
#
from random import randint
import random

def generate_numbers(n):
    """번호 뽑기"""
    return random.sample(range(1, 45), n)

def draw_winning_numbers():
    """당첨 번호 뽑기"""
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
    """겹치는 번호 개수"""
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count

def check(numbers, winning_numbers):
    """당첨 확인"""
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 100000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# 다운로드한 파일을 lottery.py와 같은 디렉토리에 넣고 lottery_driver.py 파일을 실행해 주세요. 현재 커서가 lottery_driver.py 파일에 있다면 아래와 같이 단축키로 '현재 파일'을 실행할 수 있습니다.(기본 Keymap 설정)
#
# Mac: Ctrl + Shift + R
# Windows: Ctrl + Shift + F10

# 이미지 1
# 실행한 후에는 아래 이미지처럼 lottery.html 파일이 생성될 텐데요. PyCharm을 사용하고 계신다면, lottery.html을 오른쪽 클릭한 후, Open in - Browser 메뉴에서 원하는 브라우저로 열어 주세요.

# 이미지 2
# HTML 파일은 웹사이트에 그림을 그려 주는 역할이라고 생각하시면 되는데요. 이 파일은 시뮬레이션 결과를 브라우저에서 시각적으로 보여 줍니다.
#
# 모든 과정이 올바르게 진행되었다면, 브라우저에 아래와 같은 결과가 나올 것입니다.

# 만약 제대로 나오지 않는다면, 앞선 과제들을 다시 보며 함수가 제대로 작성되었는지 확인해 보세요.