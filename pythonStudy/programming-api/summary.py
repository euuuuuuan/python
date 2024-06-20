# # 1. 시키는 대로 수행함
# print("Hello World")
#
# # 2. 이건 이렇다, 저건 저렇다 정의를 한 다음
# # 그걸 바탕으로 뭘 해라 시킬 수도 있음
# a = 10
# b = 20
# c = a + b
# print(c)
#
# # 3. 사용자에게 값을 받아서 실행하는 것도 가능함
# name = input("이름이 뭐에요?")
# print(f"안녕하세요! {name}씨!")
#
# search_term = input("검색어를 넣어주세요: ")
# print(f"{search_term}를 검색해쓴ㄴ데 암것도 못 찾았어요!")
#
#
# # 함수란 무엇인가
# # 4. 했던 말 다시 하기 싫은 사람들을 위해서
# # "저번에 내가 시켰던 거 있잖아 그거, 그거해!"
# def say_hello(name):
#     # 이름 넣어서 인사해!
#     print(f"안녕하세요! {name}씨")
#
#
# say_hello("양파")
#
#
# def make_ramen(ramen_name):
#     # 라면 만들어와!
#     print("물 끓이는 중...")
#     print("라면 투척했음...")
#     print("3분 기다리는 중...")
#     print("그릇에 펐음...")
#     print("젓가락이랑 김치랑 같이 들고 나가고 있음...")
#     print(f"라면{ramen_name} 나왔습니다!!!")
#
#
# make_ramen("신라면")
#
#
# def customer_handler(name, ranaking):
#     # 고객 타입에 따라서 마구마구 차별해라!
#     if ranaking == "VIP":
#         print(f"어서오십시오 우리의 매출 실적을 구해주실 호갱 {name}님!!")
#     else:
#         print(f"안녕하세요! {name}")
#
#
# customer_handler("양파", "VIP")


# def customer_handler(name, ranking, language="ko"):
#     # 월클 VIP 관!
#     greetings = {
#         "ko": {"VIP": f"어서 오십시오 우리의 매출 실적을 구해주실 호갱 {name}님!!",
#                "normal": f"안녕하세요! {name}씨"},
#         "fr": {"VIP": f"Tu vas nous donner beaucoup d'argent!! Nous t'aimons {name}!!",
#                "normal": f"Salut! {name}, une personne de valeur base"}
#     }
#     if ranking == "VIP":
#         print(greetings[language]["VIP"])
#     else:
#         print(greetings[language]["normal"])
#
#
# customer_handler("양파", "normal", "ko")
# customer_handler("Oignon", "VIP", "fr")
# customer_handler("양파", "VIP")
#
#
def simple_calculator(operation, a, b):
    """
    기본 산술 연산을 수행하는 간단한 계산기 함수입니다.

    인수:
    operation (str): 수행할 연산, 'add', 'substract', 'multiply', 또는 'divide'가 될 수 있습니다.
    a (float): 첫 번째 숫자,
    b (float): 두 번째 숫자.

    반환값:
    float 또는 str: 산술 연산의 결과 또는 오류 메시지.
    """
    if operation == 'add':
        return a + b
    elif operation == 'substract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return "오류: 0으로 나누기는 허용되지 않습니다."
        else:
            return a / b
    else:
        return "잘못된 연산입니다. 'add', 'substract', 'multiply', 'divide' 중에서 선택해주세요."


print(simple_calculator('add', 5, 3))
