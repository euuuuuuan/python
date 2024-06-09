
eng_dic = []
with open('vocabulary.txt', 'a', encoding='UTF-8') as f:
    while True:
        f.write(input("영어 단어를 입력하세요: "))
        f.write(input("한국어 뜻을 입력하세요: "))



# for line in f:
#     print(line)