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

# with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]
#         guess = input(f"{korean_word}: ")
#         if guess == "q":
#             print("단어장을 종료합니다.")
#             break
#
#         if guess == english_word:
#             print("맞았습니다!")
#         else:
#             print(f"아쉽습니다. 정답은 {english_word}입니다.")


# 해설
# 영어 단어와 한국어 뜻 받아 오기
# 파일을 읽기 위해서는 먼저 파일을 열어야겠죠?
#
#
# with open('vocabulary.txt', 'r') as f:
# 이렇게 하면 vocabulary.txt라는 파일을 열고, 그 파일을 읽을 수 있습니다. 이제 파일을 한 줄씩 순서대로 읽어야 하는데요. for문을 사용하면 되겠죠?
#
#
# for line in f:
# for문의 수행 부분에는 어떤 코드가 들어가야 할까요? 먼저 각 줄(line)의 영어 단어와 한국어 뜻을 각각 어떻게 받아 올 수 있을지 생각해 봅시다. 두 단계를 거쳐 받아 올 수 있는데요.
#
# strip을 이용해서 line에서 "\n"을 없앤다.
# split을 이용해서 영어 단어와 한국어 뜻 나눈다.
# 코드로 작성하면 이렇습니다.
#
#
# data = line.strip().split(": ")
# 그러면 data 리스트의 0번 인덱스에는 영어 단어가 들어가고, 1번 인덱스에는 한국어 뜻이 들어가는 거죠. 깔끔한 코드를 위해, 각각 변수에 할당하겠습니다.
#
#
# english_word, korean_word = data[0], data[1]
# 문제 내기
# 이제 사용자에게 문제를 내고, 답을 입력 받으면 됩니다.
#
#
# guess = input("{}: ".format(korean_word))
# 그 후에는 답이 맞았는지 틀렸는지 알려 주는 코드만 작성하면 되는데요. 이렇게 할 수 있습니다.
#
#
# if guess == english_word:
#     print("맞았습니다!\n")
# else:
#     print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
# 모범 답안
#
# with open('vocabulary.txt', 'r') as f:
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]
#
#         # 유저 입력값 받기
#         guess = input("{}: ".format(korean_word))
#
#         # 정답 확인하기
#         if guess == english_word:
#             print("맞았습니다!\n")
#         else:
#             print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))


# 실습 설명
# 지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요.
# 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.
# 이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을
# 랜덤한 순서로 문제를 내도록 프로그램을 바꿔 보세요.
# 같은 단어를 여러 번 물어봐도 괜찮고,
# 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.

import random
vocab = {} # list

with (open('vocabulary.txt', 'r', encoding='UTF-8') as f):
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

        keys = list(vocab.keys())

while True:
    index = random.randint(0, len(keys) -1)
    english_word = keys[index]
    korean_word = vocab[english_word]

    guess = input(f"{english_word}: ")
    if guess == "q":
        print("단어장을 종료합니다.")
        break

    if guess == korean_word:
        print("맞았습니다!")
    else:
        print(f"아쉽습니다. 정답은 {korean_word}입니다.")

# 해설
# 이 프로그램은 크게 두 단계로 나뉩니다.
#
# vocabulary.txt에 있는 단어와 뜻을 파이썬 사전에 정리한다.
# 사전에 있는 단어 중 랜덤하게 골라서 문제를 낸다.
# 1. 사전 정리
# 우선 vocabulary.txt 파일을 읽고, 파이썬 사전을 채워 넣겠습니다.
#
#
# vocab = {}
# with open('vocabulary.txt', 'r') as f:
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]
#         vocab[english_word] = korean_word
# 이렇게 하면 파일에 있는 단어와 뜻이 모두 vocab 사전에 정리되겠죠? 영어 단어 목록을 받아 오려면 파이썬 사전의 keys를 사용하면 되는데요. keys라는 변수에 저장해 줍시다.
#
#
# keys = list(vocab.keys())
# 2. 문제 내기
# 문제를 내는 부분은 코드가 조금 더 복잡합니다. 이 중에서도 가장 헷갈릴 만한 부분은 랜덤한 문제를 받아 오는 것입니다. 우선 한국어 단어는 배제하고 생각해 봅시다.
#
# random 모듈의 randint() 함수를 이용해서 랜덤한 인덱스를 받는다.
# 그 랜덤한 인덱스를 통해 vocab.keys() 리스트에서 단어를 받는다.
# 코드로 표현하면 이렇습니다.
#
#
# index = random.randint(0, len(keys) - 1)
# english_word = keys[index]
# 그리고 이제 이에 해당하는 한국어 뜻을 받아 오는 것은 너무 쉽습니다.
#
#
# korean_word = vocab[english_word]
# 나머지 부분은 앞선 실습과 거의 똑같습니다.
#
# 유저에게 단어를 입력 받는다.
# 만약 유저가 q를 입력했으면 프로그램을 종료한다.
# 유저가 입력한 영어 단어가 정답인지 확인한다.
# 모범 답안
#
# import random
#
# # 사전 만들기
# vocab = {}
# with open('vocabulary.txt', 'r') as f:
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]
#         vocab[english_word] = korean_word
#
# # 목록 가져오기
# keys = list(vocab.keys())
#
# # 문제 내기
# while True:
#     # 랜덤한 문제 받아 오기
#     index = random.randint(0, len(keys) - 1)
#     english_word = keys[index]
#     korean_word = vocab[english_word]
#
#     # 유저 입력값 받기
#     guess = input("{}: ".format(korean_word))
#
#     # 프로그램 끝내기
#     if guess == 'q':
#         break
#
#     # 정답 확인하기
#     if guess == english_word:
#         print("정답입니다!\n")
#     else:
#         print("틀렸습니다. 정답은 {}입니다.\n".format(english_word))