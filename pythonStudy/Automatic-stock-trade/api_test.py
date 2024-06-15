# 쿼리 파라미터 보내기
# import requests
#
# url = "http://learn.codeit.kr/api/avatars"
# params = {"limit": 5, "offset": 10}
# try:
#     res = requests.get(url, params=params)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
    # limit: 응답에서 반환할 최대 항목 수를 지정합니다.
    # offset: 반환하기 시작하기 전에 건너뛸 항목 수를 지정합니다.
    # 실제 사용 예를 들어 설명하자면:
    #
    # limit이 5이고 offset이 0이면 처음 5개의 항목을 가져옵니다.
    # limit이 5이고 offset이 5이면 처음 5개를 건너뛰고 그 다음 5개의 항목을 가져옵니다.
    # limit이 5이고 offset이 10이면 처음 10개를 건너뛰고 11번째 항목부터 5개의 항목을 가져옵니다.

# POST 리퀘스트로 바디 보내 보기
# import requests
#
# url = "https://learn.codeit.kr/api/avatars"
# headers = {"Content-Type": "application/json"}
# # headers 사전은 "Content-Type"이라는 키와 "application/json"이라는 값을 갖고 있습니다.
# body = {"hairType": "short2", "hairColor": "brown", "skin": "tone200", "clothes": "hoodie", "accessories": "earbuds"}
# # body 사전은 여러 키-값 쌍을 포함하고 있습니다.
# try:
#     # 아규먼트(argument)는 함수나 메서드를 호출할 때 함수에 전달되는 실제 값이나 변수를 말합니다.
#     # 코드에서 requests.post 함수는 여러 아규먼트를 받습니다. 예를 들어, url, headers, json 등이 있습니다.
#     # 여기서 url, headers=headers, json=body는 requests.post 함수에 전달되는 아규먼트입니다.
#     res = requests.post(url, headers=headers, json=body)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)

# 요약:
# 사전은 키-값 쌍으로 데이터를 저장하는 자료구조입니다. 코드에서 headers와 body는 사전입니다.
# 아규먼트는 함수 호출 시 함수에 전달되는 실제 값이나 변수를 의미합니다.
# 코드에서 url, headers=headers, json=body는 requests.post 함수에 전달되는 아규먼트입니다.

# f-string으로 리퀘스트 보내기
# 이번엔 생성한 데이터를 한 번 조회해 볼게요.
# 예를 들어서 아이디 값이 예를 들어 10이라면
# https://learn.it.kr/api/avatars/10 이렇게 슬래시를 적고
# 아이디 값을 붙인 주소로 GET 리퀘스트를 보내면 됩니다.
# 여기까지 따라해 보셨다면, 내가 생성한 데이터를 조회하는 코드를 한 번 직접 작성해 보세요.
#
# 아래는 avatar_id라는 변수를 만들고 f-string으로 주소를 바꿀 수 있게 만들어 본 코드입니다. 이렇게 작성하면 좀 더 코드를 수정하기 쉽겠죠?
#
# 앞으로 f-string을 많이 사용할 건데요.
# 앞에서 간단하게만 살펴봤기 때문에 잘 기억나지 않으실 겁니다.
# [문자열을 포매팅하는 다양한 방식]에서 f-string을 사용하는 방법을 한번 확인해 보세요.

# import requests
#
# avatar_id = 373
# url = f"https://learn.it.kr/api/avatars/{avatar_id}"
# try:
#     res = requests.get(url)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)

# GET 메소드로 쿼리 파라미터 함께 보내기
# GET https://learn.it.kr/api/avatars?limit=5&offset=10

# import requests # 모듈을 불러옵니다.
#
# url = "https://learn.it.kr/api/avatars" # 리퀘스트를 보낼 주소
# params = {"limit": 5, "offset": 10} # 쿼리 파라미터
# try:
#     # url에 적은 주소에 GET 메소드로 params에 지정한 쿼리 파라미터와 함께 리퀘스트를 보낸다.
#     res = requests.get(url, params=params)
#     # 받은 리스폰스의 바디는 JSON 형태이기 때문에 `json()` 함수를 사용해서 파이썬 사전으로 변환한다.
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)

