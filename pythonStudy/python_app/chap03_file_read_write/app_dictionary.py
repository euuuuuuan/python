# 영어 강사 Coy는 학생들의 단어 암기를 위해 단어장 프로그램을 만들려고 합니다. 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요. 사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다. 사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다. 사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 합니다.
#
# 실습 결과
# 프로그램의 예시 동작은 아래와 같습니다.
#
#
# 영어 단어를 입력하세요:
#
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요:
#
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요:
#
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요:
#
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요: 사과
# 영어 단어를 입력하세요:
# 이런 식으로 단어를 8개 입력했다고 가정합시다.
#
#
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요: 사과
# 영어 단어를 입력하세요: church
# 한국어 뜻을 입력하세요: 교회
# 영어 단어를 입력하세요: temple
# 한국어 뜻을 입력하세요: 절
# 영어 단어를 입력하세요: wallet
# 한국어 뜻을 입력하세요: 지갑
# 영어 단어를 입력하세요: backpack
# 한국어 뜻을 입력하세요: 책가방
# 영어 단어를 입력하세요: soap
# 한국어 뜻을 입력하세요: 비누
# 영어 단어를 입력하세요: bicycle
# 한국어 뜻을 입력하세요: 자전거
# 영어 단어를 입력하세요: q
# 사용자가 q를 입력하면 프로그램이 종료되고, vocabulary.txt에 다음과 같이 단어들이 정리되어 있어야 합니다.
#
#
# cat: 고양이
# apple: 사과
# church: 교회
# temple: 절
# wallet: 지갑
# backpack: 책가방
# soap: 비누
# bicycle: 자전거


# 나의 문제 해결
# with open('vocabulary.txt', 'w', encoding='UTF-8') as f:
#     while True:
#         eng_dic = input("영어 단어를 입력하세요: ")
#         if eng_dic == "q":
#             print("단어장 입력을 종료합니다.")
#             break
#
#         kor_dic = input("한국어 뜻을 입력하세요: ")
#         if kor_dic == "q":
#             print("단어장 입력을 종료합니다.")
#             break
#
#         f.write(f"{eng_dic}: {kor_dic}\n")


        # merge_eng_dic[0] = eng_dic
        # merge_kor_dic[1] = kor_dic


        # if f.write(input("q")) == "q":
        #     break


# 해설
# 파일을 쓰기 위해서는 먼저 파일을 열어야겠죠?
#
#
# with open('vocabulary.txt', 'w') as f:
# 이렇게 하면 vocabulary.txt라는 파일을 열고, 그 파일에 글을 작성할 수 있습니다. 글을 작성하기 위해서는 단어와 뜻을 반복적으로 받아야 하는데요. while문에서 반복적으로 해야 하는 일을 정리해 봅시다.
#
# 영어 단어를 입력 받는다.
# 만약 유저가 q를 입력했으면 프로그램을 종료한다.
# 한국어 뜻을 받는다.
# 만약 유저가 q를 입력했으면 프로그램을 종료한다.
# 영어 단어와 한국어 뜻을 단어: 뜻의 형태로 파일에 작성한다.
# 이것을 코드로 변환하기만 하면 됩니다.
#
# 모범 답안
#
# with open('vocabulary.txt', 'w') as f:
#     while True:
#         english_word = input('영어 단어를 입력하세요: ')
#         if english_word == 'q':
#             break
#
#         korean_word = input('한국어 뜻을 입력하세요: ')
#         if korean_word == 'q':
#             break
#
#         f.write('{}: {}\n'.format(english_word, korean_word))


# 실습 2 설명
# 실습 설명
# 이번 실습은 코드잇 실행기가 지원되지 않습니다. 자신의 컴퓨터에서 실습을 진행하고, 셀프 채점 버튼을 눌러 채점해 보세요.
# 앞선 실습에서 vocabulary.txt라는 파일을 만들었죠? 이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있는데요. 이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내는 프로그램을 만들려고 합니다.
#
# 프로그램은 터미널에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다. 사용자가 입력한 영어 단어가 정답이면 맞았습니다!라고 출력하고, 틀리면 아쉽습니다. 정답은 OOO입니다.가 출력되어야 합니다.
#
# 문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.
#
# 실습 결과
#
# 고양이: cat
# 맞았습니다!
#
# 사과: fruit
# 아쉽습니다. 정답은 apple입니다.
#
# 교회: church
# 맞았습니다!
#
# 절: tample
# 아쉽습니다. 정답은 temple입니다.
#
# 지갑: wallet
# 맞았습니다!

# 나의 문제 해결

QUESTION = ""
CORRECTION = ""
answer = ""

with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        answer = input(f"{QUESTION}: ")
        if answer == QUESTION:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {CORRECTION}입니다.")