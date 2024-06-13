# 사전 (dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary)) # 사전자료형 dict가 출력
print(my_dictionary[3])

my_dictionary[9] = 81
print(my_dictionary)
# 순서라는 개념이 없다.
# 사전의 키 값은 정수형일 필요가 없다.
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진'
}
print(my_family['아빠'])

# 실습 1 설명
# 태호는 미국 다트머스 대학교 컴퓨터 과학과에 지원하려고 합니다.
# 컴퓨터 과학 전공으로 미국 유학을 가고 싶기 때문에,
# 코딩 공부와 영어 공부를 모두 해야 하는 상황인데요.
# 그 둘을 동시에 하기 위해서 파이썬으로 단어장 프로그램을 만들기로 합니다.
#
# 해야 할 일
# 단어장 만들기
# 새로운 단어들 추가
# 1. 단어장 만들기
# 잘 모르는 단어 네 개입니다.
#
# sanitizer: 살균제
# ambition: 야망
# conscience: 양심
# civilization: 문명
# 이 단어들을 저장하는 사전을 만들고,
# 만든 사전을 vocab라는 변수에 저장하세요.
# 단어와 뜻이 key-value로 들어가야 합니다.
#
# 2. 새로운 단어들 추가
# 이미 만들어진 vocab 사전에 새로운 단어들을 추가하고 싶습니다.
# 아래 단어들을 추가해 주세요.
#
# privilege: 특권
# principle: 원칙
# 실습 결과
#
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심', 'civilization': '문명'}
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심', 'civilization': '문명', 'privilege': '특권', 'principle': '원칙'}

# 나의 문제 해결
vocab = {
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}
print(vocab)
vocab["privilege"] = "특권"
vocab["principle"] = "원칙"
print(vocab)

# 해설
# 1. 단어장 만들기
# 사전을 만들기 위해서는 괄호를 열고 닫고, 그 사이에 원하는 쌍(pair)들을 추가하면 됩니다.
#
#
# vocab = {
#     'sanitizer': '살균제',
#     'ambition': '야망',
#     'conscience': '양심',
#     'civilization': '문명'
# }
# 2. 새로운 단어들 추가
# vocab 사전에 새로운 key-value 쌍을 추가하기 위해서는 vocab[key] = value의 형태로 코드를 쓰면 됩니다.
#
#
# vocab['privilege'] = '특권'
# vocab['principle'] = '원칙'
# 모범 답안
#
# # 1. 단어장 만들기
# vocab = {
#     'sanitizer': '살균제',
#     'ambition': '야망',
#     'conscience': '양심',
#     'civilization': '문명'
# }
# print(vocab)
#
#
# # 2. 새로운 단어들 추가
# vocab['privilege'] = '특권'
# vocab['principle'] = '원칙'
# print(vocab)


# 사전 활용법
my_family1 = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동진',
    '딸': '이지영',
}

print(my_family1.values())
print('이지영' in my_family1.values())
print('성태호' in my_family1.values())
for value in my_family1.values():
    print(value)

print(my_family1.keys())
for key in my_family1.keys():
    value = my_family1[key]
    print(key, value)

print()
for key, value in my_family1.items():
    print(key, value)


# 실습 2 설명
# 태호는 영어 단어 공부를 위해서 단어장 프로그램을 만들었습니다.
# 하지만 이번에는 영-한으로 공부하는 것이 아니라, 한-영으로 공부를 해 보고 싶습니다.
#
# 사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요.
# reverse_dict는 파라미터로 사전 old_dict를 받고,
# key와 value가 뒤집힌 새로운 사전을 리턴합니다.
# 영-한 단어장
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심',
# 'civilization': '문명', 'privilege': '특권', 'principles': '원칙'}
#
# 한-영 단어장
# {'살균제': 'sanitizer', '야망': 'ambition', '양심': 'conscience',
# '문명': 'civilization', '특권': 'privilege', '원칙': 'principles'}

print()
# 나의 문제 해결
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(old_dict):
    new_dict = {}  # 새로운 사전
    # old_dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in old_dict.items():
        # new_dict[key] = value
        # print(new_dict[key])
        new_dict[value] = key
        # print(new_dict[value])

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# 해설
# old_dict의 key와 value를 모두 받아오려면 어떻게 해야 할까요?
#
# 이렇게 하면 됩니다.
#
#
# for key, value in old_dict.items():
# 각 key-value 쌍을 new_dict에 저장하고 싶은 건데요. new_dict[key] = value를 하면 기존 old_dict와 똑같은 사전이 만들어집니다. new_dict[value] = key를 해야 뒤집힌 사전을 만들 수 있겠죠?
#
# 모범 답안
#
# # 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
# def reverse_dict(old_dict):
#     new_dict = {}  # 새로운 사전
#
#     # old_dict의 key와 value를 뒤집어서 new_dict에 저장
#     for key, value in old_dict.items():
#         new_dict[value] = key
#
#     return new_dict  # 변환한 새로운 사전 리턴
#
#
# # 영-한 단어장
# vocab = {
#     'sanitizer': '살균제',
#     'ambition': '야망',
#     'conscience': '양심',
#     'civilization': '문명',
#     'privilege': '특권',
#     'principles': '원칙'
# }
#
# # 기존 단어장 출력
# print("영-한 단어장\n{}\n".format(vocab))
#
# # 변환된 단어장 출력
# reversed_vocab = reverse_dict(vocab)
# print("한-영 단어장\n{}".format(reversed_vocab))


# 실습 3 설명
# 효신이는 매년 국회의원 선거 때마다, 성북구에서 집계 도우미 봉사를 하는데요.
# 작년까지는 표를 손수 세다가, 올해부터는 IT 시대에 더 적합한 솔루션을 개발하려고 합니다.
#
# 파이썬 리스트 votes에는 성북구민들의 투표 결과가 저장되어 있습니다.
# 리스트 votes의 정보를 토대로, 사전 vote_counter에
# 후보별 득표수를 정리하는 것이 목표입니다.
#
# 예를 들어서 votes가
# ['허유나', '서혜선', '허유나']라고 가정하면,
# vote_counter는 {'허유나': 2, '서혜선': 1}이 되어야 하는 거죠.

# 실습 결과
# {'김영자': 11, '강승기': 6, '최만수': 8}

print()
# 나의 문제 해결
# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
         '최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
         '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name in vote_counter:
        vote_counter[name] += 1
    else:
        vote_counter[name] = 1

# 후보별 득표수 출력
print(vote_counter)

# 해설
# for문을 이용해서 votes에 있는 후보 이름을 순서대로 name이라는 변수에 지정합니다. name을 vote_counter 사전에 반영하면 되는데요. 두 가지 경우가 있습니다.
#
# 해당 후보(name)가 아직 vote_counter에 없는 케이스
# 해당 후보(name)가 이미 vote_counter에 있는 케이스
# 1번 케이스는 해당 후보가 첫 득표를 한 상황인데요. 그러면 그냥 vote_counter[name] = 1을 하면 되겠죠?
#
# 2번 케이스는 해당 후보가 이미 최소 하나의 득표를 한 상황입니다. 이 경우 기존 득표 수에 1을 늘려 주면 되는데요. 그러면 vote_counter[name] += 1을 하면 됩니다.
#
# 모범 답안
# # 투표 결과 리스트
# votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
# '최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
# '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']
#
# # 후보별 득표수 사전
# vote_counter = {}
#
# # 리스트 votes를 이용해서 사전 vote_counter를 정리하기
# for name in votes:
#     if name not in vote_counter:
#         vote_counter[name] = 1
#     else:
#         vote_counter[name] += 1
#
# # 후보별 득표수 출력
# print(vote_counter)

