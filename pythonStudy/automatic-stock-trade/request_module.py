# 이번 레슨에서는 파이썬으로 리퀘스트를 보내는 방법과 리스폰스를 받아서 사용하는 방법을 배워 볼게요.
#
# requests라는 모듈에 대해 배울 건데요. 혹시 파이썬 문법에서 배웠던 import 기억하시나요? import를 써서 다른 파이썬 파일에 있는 코드를 불러와서 쓰거나, 다른 사람이 미리 코딩해 놓은 코드, 즉 파이썬 모듈을 불러와서 쓸 수 있었습니다. requests는 파이썬에서 기본으로 제공하는 모듈은 아니지만 네트워크를 다룰 때 가장 많이 쓰는 모듈입니다. 이번 레슨에서는 requests로 리퀘스트를 보내고 받은 리스폰스를 사용해 볼 거예요.
#
# 앞에서는 구글 크롬으로 리퀘스트를 보내고 리스폰스를 받았었죠. 코드잇 실습 서버가 서버 역할을 하고, 웹 브라우저가 클라이언트 역할을 했었습니다. 이번에는 구글 크롬 대신에 파이썬 프로그램이 클라이언트 역할을 하는 걸 만들 거예요. 말만 들으면 어려워 보이는데, 앞에서 해 봤던 거랑 똑같아요. 웹 브라우저 대신에 파이썬 모듈을 사용하다는 점만 다릅니다. 주소창에 주소를 입력했듯이 리퀘스트를 보낼 주소를 파이썬 코드에 잘 적어서 실행하면 나머지는 모듈이 알아서 해 줄 겁니다.

# 리퀘스트 보내기
# 일단 api_test.py라는 파이썬 파일을 하나 만들고 코드를 적어 보겠습니다.
#
#  api_test.py
#
#
# import requests
#
# url = "https://learn.codeit.kr/api/avatars"
# res = requests.get(url)
# try:
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# 메소드
#
# requests라는 모듈을 불러와서 requests.get() 함수를 가지고 GET 리퀘스트를 보내는 코드입니다. 이런 식으로 리퀘스트 메소드에 따라서 GET 메소드면 requests.get(), POST 메소드면 requests.post() 함수를 쓰면 됩니다.
#
# 리스폰스
#
# requests 모듈에서는 리퀘스트를 보내면 리스폰스에 해당하는 값을 리턴하는데요. 이걸 res 라는 변수에 저장했습니다.
#
# try-except문
#
# 그러고 나서 특이한 문법이 있죠. 이건 try-except문이라는 건데요. 이 문법은 실패할 가능성이 있는 코드를 try: 블록에서 실행하고 만약에 예외적인 상황이 발생하면 except: 블록에 있는 코드를 실행해 줍니다.
#
# 네트워크 리퀘스트는 항상 100% 성공할 수는 없잖아요? 그래서 이런 식으로 try: 블록 안에다가 실행할 코드를 써 주고, except Except as e: 블록에서는 예외적인 상황이 발생했을 때 print(e)로 출력해 주는 거죠. 리퀘스트를 보내는 코드에선 되도록이면 이렇게 try-except문을 사용하는 걸 권장드려요.
#
# JSON 사용하기
#
# 아까 잠깐 살펴봤었는데, 실습 서버에서는 리스폰스로 바디에 JSON 데이터를 보내 주고 있었죠? 그래서 json() 함수로 JSON 데이터를 파이썬 사전형으로 변환했습니다.
#
# PyCharm에서 오른쪽 위에 있는 실행 버튼을 눌러서 코드를 실행해 보면 아래와 같이 아까 전에 구글 크롬에서 봤던 리스폰스 바디가 잘 출력되는 걸 알 수 있습니다.
#
# 받아 온 아바타 데이터가 잘 보이시나요?
#
# 3jdbwf2wx-image.png
#
# 쿼리 파라미터 보내기
# 앞에서 ?limit=5&offset=10이라는 주소 살펴봤던 거 기억 나시나요? 이런 걸 쿼리 파라미터라고 부르는데요.
#
# 참고로 실습 서버에서 limit이라는 쿼리 파라미터는 데이터를 받아 올 개수를 정하는 옵션 같은 거예요. limit의 값이 5면 데이터를 다섯 개만 가져옵니다(참고로 이 내용은 코드잇 실습 서버에서 정한 규칙이니 자세히 몰라도 괜찮습니다).
#
# 파이썬에서는 쿼리 파라미터를 이렇게 일일이 적어 주지 않고 함수의 아규먼트로 전달해 줄 수 있어요. 파이썬 사전을 써서 합니다. 아래와 같은 사전을 만들 거예요.
#
#
# params = {"limit": 5, "offset": 10}
# 그리고 이걸 requests.get() 함수에 params라는 이름의 아규먼트로 전달해 보세요.
#
#  api_test.py
#
#
# import requests
#
# url = "https://learn.codeit.kr/api/avatars"
# params = {"limit": 5, "offset": 10}
# try:
#     res = requests.get(url, params=params)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# vaae3ppy4-image.png
#
# 이 코드를 실행했을 때 출력된 값을 복사해서 한번 살펴보죠. (참고로 서버에 있는 데이터는 변할 수 있기 때문에 여러분이 받은 데이터랑은 값이 다를 수 있습니다.)
#
#
# {'count': 137, 'next': 'https://learn.codeit.kr/api/avatars/?limit=5&offset=15', 'previous': 'https://learn.codeit.kr/api/avatars/?limit=5&offset=5', 'results': [{'createdAt': 1715571789000, 'updatedAt': 1715571789000, 'id': 127, 'hairType': 'long1', 'hairColor': 'black', 'skin': 'tone100', 'clothes': 'hoodie', 'accessories': 'none'}, {'createdAt': 1715571473000, 'updatedAt': 1715571473000, 'id': 126, 'hairType': 'long1', 'hairColor': 'black', 'skin': 'tone100', 'clothes': 'hoodie', 'accessories': 'none'}, {'createdAt': 1715571469000, 'updatedAt': 1715571469000, 'id': 125, 'hairType': 'long1', 'hairColor': 'black', 'skin': 'tone100', 'clothes': 'hoodie', 'accessories': 'none'}, {'createdAt': 1715571413000, 'updatedAt': 1715571413000, 'id': 124, 'hairType': 'long1', 'hairColor': 'black', 'skin': 'tone100', 'clothes': 'hoodie', 'accessories': 'none'}, {'createdAt': 1715566362000, 'updatedAt': 1715566362000, 'id': 123, 'hairType': 'long1', 'hairColor': 'black', 'skin': 'tone100', 'clothes': 'hoodie', 'accessories': 'none'}]}
#
# test 라는 변수를 임시로 만들고 아래처럼 붙여 넣었습니다.
#
# aa1tfa3mq-image.png
#
# 이 test 변수를 코드에서 사용할 건 아니에요. 코드창에서 데이터를 확인만 해 볼 건데요. Shift 키를 두 번 눌러서 뜨는 PyCharm 명령창에서 'Reformat Code'라고 찾아보세요. 이걸 선택하면 코드를 알아서 정리해 줍니다.
#
# 1ygnin7aa-image.png
#
# 정리된 코드를 보면 results 라는 속성으로 리스트 값이 있는데요. 이 리스트에는 요소가 다섯 개 있을 겁니다. 앞에서 리퀘스트를 보낼 때 limit=5라고 보냈기 때문에 그런 거죠.
#
# 9ul6wxdvf-image.png
#
# 데이터를 다 살펴봤으니까, 임시로 적었던 코드는 다시 지워 놓겠습니다.
#
#  api_test.py
#
#
# import requests
#
# url = "https://learn.codeit.kr/api/avatars"
# params = {"limit": 5, "offset": 10}
# try:
#     res = requests.get(url, params=params)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# POST 리퀘스트로 바디 보내 보기
# 이번에는 서버에 데이터를 한번 보내 보겠습니다. 보통은 POST 메소드랑 바디를 보내면 새로운 데이터를 생성할 수 있는데요, 코드잇 실습 서버에서는 https://learn.codeit.kr/api/avatars라는 주소로 POST 메소드 리퀘스트를 보내면 새로운 아바타를 생성할 수 있어요.
#
# 코드잇에서 제공하는 Avatar API 문서에는 아래와 같이 예시 리퀘스트가 나와 있습니다.
#
#
# POST https://learn.codeit.kr/api/avatars
# Content-Type: application/json
#
# {
#   "hairType": "short2",
#   "hairColor": "brown",
#   "skin": "tone200",
#   "clothes": "hoodie",
#   "accessories": "earbuds"
# }
#
# 메소드는 POST, 헤더로는 Content-Type 값을 application/json으로 보내고, 그 아래에는 생성하고 싶은 아바타 데이터를 바디로 적은 거예요. 바디는 앞에서 살펴보았던 JSON의 형태입니다. 앞에서 썼던 코드를 바꿔 놓고 하나씩 설명드릴게요.
#
#  api_test.py
#
#
# import requests
#
# url = "https://learn.codeit.kr/api/avatars"
# headers = {"Content-Type": "application/json"}
# body = {"hairType": "short2", "hairColor": "brown", "skin": "tone200", "clothes": "hoodie", "accessories": "earbuds"}
# try:
#     res = requests.post(url, headers=headers, json=body)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
# 우선 POST 메소드로 보낼 거니까 requests.post() 함수를 썼고요, 헤더 값은 headers라는 사전을 만들어서 headers라는 아규먼트로 넘겨줬습니다.
#
# 그리고 바디로 보낼 데이터는 body라는 사전으로 만들었는데요. 이건 JSON 데이터 형식으로 보낼 거기 때문에 json이라는 아규먼트로 보냈습니다.
#
# 제대로 리퀘스트를 보냈다면 출력 값으로 생성된 아바타 데이터가 보일 겁니다. 서버에서 리스폰스로 보내 준 거예요. 보시면 id라는 값이 있을 건데요. 이 아이디 값으로 내가 생성한 데이터를 조회할 수 있어요. 데이터를 생성할 때마다 붙여 주는 아이디니까, 여러분이 받은 아이디 값은 다를 수 있습니다.
#
# f-string으로 리퀘스트 보내기
# 이번엔 생성한 데이터를 한 번 조회해 볼게요. 예를 들어서 아이디 값이 예를 들어 10이라면 https://learn.codeit.kr/api/avatars/10 이렇게 슬래시를 적고 아이디 값을 붙인 주소로 GET 리퀘스트를 보내면 됩니다. 여기까지 따라해 보셨다면, 내가 생성한 데이터를 조회하는 코드를 한 번 직접 작성해 보세요.
#
# 아래는 avatar_id라는 변수를 만들고 f-string으로 주소를 바꿀 수 있게 만들어 본 코드입니다. 이렇게 작성하면 좀 더 코드를 수정하기 쉽겠죠?
#
# 앞으로 f-string을 많이 사용할 건데요. 앞에서 간단하게만 살펴봤기 때문에 잘 기억나지 않으실 겁니다. [문자열을 포매팅하는 다양한 방식]에서 f-string을 사용하는 방법을 한번 확인해 보세요.
#
#
# import requests
#
# avatar_id = 10
# url = f"https://learn.codeit.kr/api/avatars/{avatar_id}"
# try:
#     res = requests.get(url)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# 정리
# 지금까지 배운 requests 사용법을 코드와 함께 코멘트로 정리해 보겠습니다. 앞으로 프로젝트를 진행하면서 아래 코드를 자유롭게 활용해 보시기 바랍니다.
#
# GET 메소드로 쿼리 파라미터 함께 보내기
# 리퀘스트 예시
#
#
# GET https://learn.codeit.kr/api/avatars?limit=5&offset=10
# 파이썬 예시
#
#
# import requests # 모듈을 불러옵니다.
#
# url = "https://learn.codeit.kr/api/avatars" # 리퀘스트를 보낼 주소
# params = {"limit": 5, "offset": 10} # 쿼리 파라미터
# try:
#     # url에 적은 주소에 GET 메소드로 params에 지정한 쿼리 파라미터와 함께 리퀘스트를 보낸다.
#     res = requests.get(url, params=params)
#     # 받은 리스폰스의 바디는 JSON 형태이기 때문에 `json()` 함수를 사용해서 파이썬 사전으로 변환한다.
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# POST 메소드로 헤더, 바디 보내기
# 리퀘스트 예시
#
#
# POST https://learn.codeit.kr/api/avatars
# Content-Type: application/json
#
# {
#   "hairType": "short2",
#   "hairColor": "brown",
#   "skin": "tone200",
#   "clothes": "hoodie",
#   "accessories": "earbuds"
# }
#
# 파이썬 예시
#
#
#
# import requests
#
# url = "https://learn.codeit.kr/api/avatars" # 리퀘스트를 보낼 주소
# headers = {"Content-Type": "application/json"} # 헤더
# body = {"hairType": "short2", "hairColor": "brown", "skin": "tone200", "clothes": "hoodie", "accessories": "earbuds"} # 바디
# try:
#     # 메소드 POST로 보내기. JSON 데이터를 보내려면 json 파라미터를 사용
#     res = requests.post(url, headers=headers, json=body)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# f-string으로 리퀘스트 보내기
# 리퀘스트 예시
#
# (:id는 조회할 데이터의 아이디가 들어가는 부분)
#
#
# GET https://learn.codeit.kr/api/avatars/:id
# 파이썬 예시
#
#
# import requests
#
# avatar_id = 10
# url = f"https://learn.codeit.kr/api/avatars/{avatar_id}"
# try:
#     res = requests.get(url)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)

# 받은 리스폰스가 JSON 형태인지는 일반적으로 API의 문서나 서버의 응답 헤더를 통해 알 수 있습니다. JSON 형식의 리스폰스는 주로 Content-Type 헤더에 application/json이 명시되어 있습니다. 이를 확인하는 방법은 다음과 같습니다:

# 1. API 문서 확인
# API를 제공하는 서비스의 문서를 확인하면 응답 형식이 명시되어 있습니다. 문서에서 응답이 JSON 형식임을 명시하고 있으면, 리스폰스가 JSON 형식임을 알 수 있습니다.

# 2. 응답 헤더 확인
# 리스폰스의 Content-Type 헤더를 확인하여 응답 데이터의 형식을 알 수 있습니다. Content-Type 헤더가 application/json이면, 응답 데이터는 JSON 형식입니다.

# 코드 예시
# 다음은 Content-Type 헤더를 확인하는 코드입니다:
#import requests

# url = "https://learn.codeit.kr/api/avatars"
# params = {"limit": 5, "offset": 10}

# try:
#    res = requests.get(url, params=params)

#    # Content-Type 헤더 확인
#    content_type = res.headers.get('Content-Type')
#    print(f"Content-Type: {content_type}")

#    # Content-Type이 application/json이면 JSON 형식으로 파싱
#    if 'application/json' in content_type:
#        data = res.json()
#        print(data)
#    else:
#        print("응답이 JSON 형식이 아닙니다.")
# except Exception as e:
#    print(e)
# 상세 설명
# API 요청: requests.get(url, params=params)로 API에 GET 요청을 보냅니다.
# Content-Type 헤더 확인: res.headers.get('Content-Type')로 응답 헤더에서 Content-Type 값을 가져옵니다.
# JSON 형식인지 확인: if 'application/json' in content_type: 조건문으로 Content-Type 헤더에 application/json이 포함되어 있는지 확인합니다.
# JSON 파싱: res.json()으로 JSON 형식의 응답을 파싱하여 파이썬 사전으로 변환합니다.