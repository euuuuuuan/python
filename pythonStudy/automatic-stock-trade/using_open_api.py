# 앞에서 코드잇 실습 서버를 가지고 파이썬을 써서 리퀘스트를 보내 봤습니다. 우리 목표는 파이썬으로 증권사에서 제공하는 서버에 리퀘스트를 보내는 건데요. 2024년을 기준으로 한국 증권사 중에서 가장 간편하게 리퀘스트를 사용할 수 있는 곳은 한국투자증권입니다. 한국투자증권에서는 API라는 걸로 데이터를 받아오고, 증권 거래를 할 수 있도록 해 주는데요.
#
# 이번 토픽에서는 API라는 게 무엇인지 간단히 살펴본 다음, 한국투자증권의 계좌를 만들고 개발자 문서를 함께 보면서 파이썬으로 리퀘스트를 보내는 것까지 해 보겠습니다.
#
# API란?
# 혹시 API라는 말 들어 보신 적 있나요? 프로그래밍에서 굉장히 자주 사용하는 말인데요. API는 '애플리케이션 프로그래밍 인터페이스(Application Programming Interface)'의 약자인데, 여기서 인터페이스는 '접점'이라는 의미입니다.
#
# '애플리케이션 프로그래밍의 접점'이니까, 애플리케이션을 만들 때 다른 사람들이 만든 프로그램을 활용해서 만들 수 있도록 만들어 놓은 접점 같은 거예요. 프로그램이 복잡해지면 복잡해질수록 모든 걸 다 직접 만들 수는 없잖아요? 그래서 미리 만들어 놓은 프로그램을 이용하기도 하고, 앞에서 살펴본 것처럼 서버랑 클라이언트가 있어서 어떤 서버를 이용하기도 해요.
#
# 예를 들면 쇼핑몰 사이트를 만든다고 해 볼게요. 쇼핑몰에선 카드 결제를 많이 하죠. 이런 카드 결제 시스템은 만드는 게 정말 복잡합니다. 그래서 대부분의 쇼핑몰은 결제 시스템을 직접 만들지 않고, 다른 결제 대행업체(Payment Gateway)를 이용해요.
#
# 그럼 어떻게 쇼핑몰 안에서 카드 결제를 할 수 있는 걸까요? 바로 결제 대행업체에서 제공하는 API를 사용하기 때문입니다. 결제 대행사에서는 결제 서비스를 프로그래밍하는 데 사용할 수 있도록 API를 만들고 서비스를 열어 줘요.
#
# 어떤 어떤 기능을 제공하고, 그 기능을 사용하려면 어떻게 해야 하는지 설명서 같은 것도 제공하는데요.  이런 걸 'API 문서'라고 부릅니다. 쇼핑몰 사이트를 만드는 사람들은 API 문서를 읽고 원하는 결제 기능을 가져와서 사용하면서 프로그래밍할 수 있는 거죠.
#
# 우리가 써 볼 증권사 API도 마찬가지입니다. 증권사의 서비스를 프로그램을 만들 때 쓸 수 있도록 증권사에서 서비스를 '접점'으로 열어 준 거고요. 우리가 사용할 한국투자증권 오픈 API는 이걸 HTTP 리퀘스트 형태로 사용할 수 있도록 제공하고 있습니다.
#
# 한국투자증권 오픈 API
# a6x9onkxn-image.png
#
# 한국투자증권에서는 별도의 프로그램 설치 없이도 리퀘스트/리스폰스만으로 서비스를 사용할 수 있는 오픈 API를 제공합니다.
#
# 그리고 API 문서도 제공을 하고 있는데요. 위 스크린샷을 보시면 어떤 주소로 어떤 메소드, 어떤 형식의 데이터를 보내야 하는지 적혀 있고 리퀘스트를 보낼 때 어떤 값을 보내야 하는지, 리스폰스로는 어떤 값을 보내 주는지 적혀 있습니다.
#
# 양이 엄청 많아 보이죠? 겁먹지 마세요. API 문서는 처음부터 끝까지 읽고 알아야 하는 건 아니고, 코딩할 때 옆에 계속 켜 두고 그때그때 확인하면서 쓰는 용도예요. 그러니까 문서를 검색하고 코드에 적용하는 요령만 알면 됩니다.
#
# 한국투자증권에서는 주식 데이터 조회, 주식 주문, 계좌 관리 등 증권사의 다양한 기능을 코드로 사용할 수 있도록 API를 제공하고 있어요. 쉽게 말해서 한국투자증권에서 적어 놓은 규칙 대로 파이썬을 써서 HTTP 리퀘스트를 보내면, 증권 앱에서 하던 일을 파이썬 코드로도 할 수 있다는 뜻입니다. 물론 모든 걸 할 수 있는 건 아니고, 증권사에서 제공하는 범위 안에서만 할 수 있죠.
#
# 대략적인 워크플로
# 한국투자증권 오픈 API는 이런 순서로 사용할 수 있어요.
#
# 계좌 개설하기: 가장 먼저 한국투자증권 서비스를 이용하려면 한국투자증권 계좌가 있어야겠죠?
# 개발자로 등록하기: API 서비스를 이용하려면 개발자로 등록하고 발급받은 app key와 app secret이라는 값이 필요해요. 개발자용 비밀번호 같은 건데요. 이것만 알고 있으면 내 계좌와 관련된 모든 걸 할 수 있기 때문에 꼭 안전한 곳에 보관하시고 잃어버리지 않도록 주의하셔야 합니다.
# 액세스 토큰 발급받기: 실제로 API를 사용할 때는 보안이 중요하기 때문에 액세스 토큰(access token), 접근 토큰이라고 부르는 인증 정보가 더 필요합니다. 아주 짧은 기간 동안 사용할 수 있는 비밀번호 같은 거예요. 앞에서 발급받은 app key와 app secret을 제시하고 access token을 발급받습니다. 한국투자증권 API를 사용할 때는 항상 토큰을 제시하고 사용해야 합니다. 한국투자증권에선 접근 토큰을 한 번 발급받으면 하루 동안 쓸 수 있어요.
# 코드로 API 리퀘스트 보내기: 이제 발급받은 인증 정보들을 가지고 API 문서에 적혀 있는 대로 리퀘스트를 보낼 수 있어요. 주식 현재가 데이터를 받아오거나, 잔고를 조회하는 등 다양한 일을 할 수 있고요. 데이터는 JSON으로 받을 수 있기 때문에 파이썬에서 JSON을 사전으로 변환해서 쓰면 됩니다. 코드를 잘 만들면, 다양한 걸 만들어 볼 수 있겠죠?
# 한국투자증권 API 준비하기
# 가입하기
# 한국투자증권 홈페이지 또는 모바일 앱에서 계좌를 개설해 주세요.
#
# 모의 투자 신청하기
# 이번 토픽에서는 모의 투자 계좌로 모든 걸 진행할 거예요. 잘못 작성한 코드가 실제 금전적인 손실을 초래할 수도 있으니까, 반드시 모의 투자로 신청하셔서 따라 하시는 걸 권장드립니다. 한국투자증권 홈페이지에서 트레이딩 > 모의투자 > 주식/선물옵션 모의투자 > 모의투자안내로 들어가셔서, 모의 투자 계좌를 신청합니다.
#
# g5i5na9i-image.png
#
# 개발자 등록하기
# 이제 한국투자증권 KIS Developers 등록을 합니다. 한국투자증권 홈페이지에서 트레이딩 > OpenAPI > KIS Developers > KIS Developers 서비스 신청하기로 들어가서 개발자 등록을 해 주세요. 등록을 하실 때는 모의 투자 계좌를 기준으로 등록하시고, 발급받은 app key와 app secret은 잃어버리지 않도록 안전한 곳에 적어서 보관하시면 됩니다.
#
# kcbc6f67d-image.png
#
# requests 모듈로 증권사 API 써 보기
# API 문서 읽는 법
# KIS Developers 사이트로 접속합시다. 이제부터 코딩하는 동안 계속 이 사이트를 열어 놓고 보게 될 거예요. API 문서를 들어가 보시면 한국투자증권에서 제공하는 API 사용법을 볼 수 있어요. 그중에서 가장 먼저 "접근토큰발급(P)" 섹션으로 들어가서 문서를 같이 살펴보겠습니다.
#
# ar5zv9bgc-image.png
#
# 복잡해 보이죠. 하지만 리퀘스트를 어떻게 보내야 하는지, 리스폰스로는 뭐가 오는지만 집중해서 파악하면 됩니다.
#
# "기본 정보"를 보시면 메소드(Method), 도메인, URL이 있죠. 그리고 Content-Type이라는 게 적혀 있습니다. 각각 리퀘스트를 보낼 때 어떤 메소드로 보내야 하는지, 어떤 주소로 보내야 하는지, 그리고 데이터 형식은 어떤 형식으로 주고받는지가 적혀 있어요. JSON이라고 적혀 있는데 대부분은 JSON 형식으로 주고받는다고 생각하시면 됩니다.
#
# 문서를 아래로 내려 보면 구체적인 리퀘스트 형식을 볼 수 있어요. 보시면 "리퀘스트(Request 부분)"에 바디(Body)가 적혀 있는 거 보이시나요? 이런 식으로 API 문서를 보면 리퀘스트 헤더, 쿼리 파라미터, 바디를 어떻게 보내야 하는지 형식을 알려 줄 거예요.
#
# 접근 토큰 받기
# 이제 "접근토큰발급" API 문서를 바탕으로 파이썬 코드를 써 볼게요. 도메인에 해당하는 주소로는 앞으로 모의 투자에서 코딩을 할 것이기 때문에 "모의 Domain"이라고 적힌 부분을 쓰면 됩니다. 이건 한 번 정해 놓고 계속 그대로 쓸 거예요. 모든 주소의 기본이 되는 주소이기 때문에 BASE_URL이라는 변수로 저장해 두고 사용했습니다. 참고로 이름을 대문자로 쓴 이유는 이 변수의 값은 앞으로 바꾸지 않을 상수이기 때문입니다.
#
# 참고로 한국투자증권에서는 리퀘스트를 보내는 경로의 대소문자를 구분하니까 주의하세요(예를 들면 tokenp는 안 되고 tokenP로 써야 됩니다!). 그래서 API 문서에 있는 건 되도록이면 눈으로 보고 입력하는 것보다 복사 붙여 넣기 하시는 걸 추천드려요.
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
#
# url = f"{BASE_URL}/oauth2/tokenP"
# res = requests.post(url)
# 문서를 보면 API에서는 바디로 데이터를 보내 줘야 하나 보네요. 표를 보면 바디에서 속성 이름이랑 값을 어떻게 써야 하는지 있습니다.
#
# grant_type이라는 속성을 하나 살펴볼게요.
#
# Type이 string이라고 되어 있으니까 gran_type이라는 바디 속성의 값은 문자열로 해야 된다는 뜻입니다.
#
# Required는 이 값이 반드시 있어야 하는 건지 여부를 Y/N로 적어둔 거 같네요. 앞으로 여기 API를 사용할 땐 특별한 일이 없다면 Required가 Y로 되어 있는 값들만 잘 채워서 보내 주면 됩니다.
#
# Description에 이 값을 어떤 값으로 써야 하는지 설명해 주고 있는데요. client_credentials라는 값으로 쓰면 된다고 적혀 있습니다. (Length가 18로 되어 있는데, "client_credentials"라는 값이 정확히 18 글자입니다.)
#
# 마찬가지로 appkey라는 걸 보면 아까 개발자 등록을 할 때 받은 app key를 넣으면 되는 거 같고요, appsecret이라는 속성에는 app secret을 넣으면 될 거 같네요.
#
# dh7ajbmvx-image.png
#
# get_token.py라는 파일을 만들고 파이썬 코드로 적어 보면 이렇습니다. 보안이 중요한 app key 값과 app secret 값은 ...으로 표현했습니다. 여러분 컴퓨터에서는 실제 값으로 적으시면 됩니다.
#
#  get_token.py
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# url = f"{BASE_URL}/oauth2/tokenP"
# headers = {
#     "Content-Type": "application/json"
# }
# body = {
#     "grant_type": "client_credentials",
#     "appkey": APPKEY,
#     "appsecret": APPSECRET
# }
# try:
#     res = requests.post(url, headers=headers, json=body)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
# app key랑 app secret 모두 바뀌지 않는 값이니까 APPKEY 그리고 APPSECRET이라는 변수로 지정해 줬어요.
#
# headers 변수에는 사전으로 Content-Type의 값을 "application/json" 으로 넣어 줬습니다. API 문서에서 JSON 형식으로 데이터를 주고받는다고 했죠. 그래서 이렇게 써 주어야 합니다.
#
# body 변수에는 API 문서에서 봤던 값을 적어 주고 json이라는 아규먼트로 넘겼어요.
#
# 이런 식으로 API 문서는 코딩하면서 켜 놓고 쓰면 돼요. 어떤 기능을 사용하고 싶다면 메소드, 헤더, 쿼리 파라미터, 바디 등을 확인합니다. 그리고 이걸 코드로 작성하는 식이죠.
#
# dki8r62j4-image.png
#
# 실행해 보면 JSON 형식의 데이터가 출력됩니다. access_token 값이 제공되는데, 일단 이 값을 잃어버리지 않도록 안전한 곳에 잘 복사/붙여 넣기 해 주세요. 참고로 이렇게 받은 토큰은 하루 동안만 사용 가능합니다. 우리는 일단 자동 매매를 단순하게 구현하기 위해서 이 값을 변수로 저장해 놓고 쓸 겁니다.
#
# 참고로 이 API는 API 문서에도 적혀 있지만, 1분에 딱 한 번 호출할 수 있고요, 이것보다 자주 호출하면 아래와 같은 오류 메시지가 리스폰스로 오니까 참고합시다.
#
#
# {'error_description': '접근토큰 발급 잠시 후 다시 시도하세요(1분당 1회)', 'error_code': 'EGW00133'}
# 당일 분봉 데이터 가져오기
# 이번에는 다른 API를 써 봅시다. API 문서에서 "주식당일분봉조회"를 보면서 일분봉 데이터를 가져오는 코드를 써 볼게요.
#
# mtpqnb965-image.png
#
# 우선 기본 정보를 보면 리퀘스트를 보낼 주소가 /uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice라는 걸 알 수 있고요, 메소드는 GET을 쓰면 되는 것 같습니다. 그리고 주고받는 데이터 형식은 JSON인 것 같습니다.
#
# i5v1mdiu2-image.png
#
# 그리고 리퀘스트 헤더를 보내면 되는지 나와 있네요. Required 값이 Y인, 즉 필수인 값들만 정리해 보면 아래와 같습니다.
#
# 여기서 조금 어렵게 느껴지는 부분은 authorization 부분일 거예요. API 문서를 보면 발급받은 접근 토큰을 authorization: Bearer ... 형태로 보내라고 되어 있습니다.
#
# 왜 이렇게 보내는지는 웹 개발과 유저 인증 개념에 익숙해지면 자연스럽게 이해하실 수 있는데요(코드잇에서는 [유저 기능 원리]라는 토픽에서 배울 수 있어요!), 일단 지금 단계에서는 "한국투자증권 API에서는 이런 형식에 맞춰서 접근토큰 값을 헤더로 보내면 된다" 정도로 알고 넘어가도 충분합니다.
#
#
# content-type: application/json; charset=utf-8
# authorization: Bearer <접근 토큰 값>
# appkey: appkey 값
# appsecret: appsecret 값
# tr_id: FHKST03010200
# custtype: P
# 그 아래에는 리퀘스트에 필요한 쿼리 파라미터가 있어요.
#
# kw2jo096l-image.png
#
# 쿼리 파라미터도 어떤 값이 필요한지 정리해 보면 아래와 같습니다. 일단 기타 구분 코드는 잘 모르니까 비워 두고요, 우리는 주식 시장 데이터를 가져올 거라서 FID_COND_MRKT_DIV_CODE 값은 J, 그리고 조회할 종목 코드는 일단 삼성전자의 코드 005930, 조회할 시간은 일단 주식 시장이 열리고 30분 후로 하겠습니다. 이러면 9시 30분 이전으로 일분봉 30개 데이터를 가져올 거예요. 즉, 9시 1분부터 9시 30분까지의 일분봉 데이터를 가져옵니다.
#
#
# FID_ETC_CLS_CODE:
# FID_COND_MRKT_DIV_CODE: J
# FID_INPUT_ISCD: 005930
# FID_INPUT_HOUR_1: 093000
# FID_PW_DATA_INCU_YN: Y
# 이번에는 get_stock_price.py라는 파일을 새로 만들고 여기까지 정리한 걸 앞에서 배웠던 requests 사용법에 적용해서 파이썬 코드로 적어 보겠습니다.
#
#  get_stock_price.py
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
#
# url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
# headers = {
#     "content-type": "application/json; charset=utf-8",
#     "authorization": f"Bearer {ACCESS_TOKEN}",
#     "appkey": APPKEY,
#     "appsecret": APPSECRET,
#     "tr_id": "FHKST03010200",
#     "custtype": "P"
# }
# params = {
#     "FID_ETC_CLS_CODE": "",
#     "FID_COND_MRKT_DIV_CODE": "J",
#     "FID_INPUT_ISCD": "005930",
#     "FID_INPUT_HOUR_1": "093000",
#     "FID_PW_DATA_INCU_YN": "Y"
# }
# try:
#     res = requests.get(url, headers=headers, params=params)
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
#
# 코드를 하나씩 살펴보자면, 우선 앞에서 받았던 접근 토큰값을 ACCESS_TOKEN이라는 변수로 정의했습니다. 앞으로 어떤 리퀘스트를 보낼 때 대부분은 이 값을 헤더에 보내게 될 거예요. 아래쪽의 url이라는 변수는 당일분봉 API에 해당하는 주소로 바꾸고, 헤더 값은 headers에 파이썬 사전으로 만들어 줬고요, 쿼리 파라미터도 params라는 사전에 저장했습니다.
#
# 코드를 실행해 보면 아래처럼 리스폰스로 일분봉 데이터가 도착합니다.
#
# ssc3t810d-image.png
#
# 이 데이터의 구조는 API 문서에서 리스폰스 바디를 설명하는 곳에서 확인할 수 있어요.
#
# 61kxqgcg1-image.png
#
# 보시면 output1라는 속성은 Type이 Object라고 적혀 있는데,  이건 쉽게 말해서 파이썬에선 사전이라고 생각하시면 되고요. output2라는 속성은 Object Array라고 되어 있는데, 사전 데이터들의 리스트라고 생각하시면 됩니다. 리스트 안에 요소로 사전들이 들어가 있는 거예요. 그 안에 있는 사전에는 일분봉에 대한 데이터가 사전 하나마다 들어가 있습니다. 보시면 주식 영업 일자 stck_bsop_date랑 체결 시간 stck_cntg_hour라던가 주식 현재가 stck_prpr 같은 데이터가 있죠?
#
# 한번 시험 삼아 출력해 볼게요.
#
#  get_stock_price.py
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# ACCESS_TOKEN = "..."
#
# url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
# headers = {
#     "content-type": "application/json; charset=utf-8",
#     "authorization": f"Bearer {ACCESS_TOKEN}",
#     "appkey": APPKEY,
#     "appsecret": APPSECRET,
#     "tr_id": "FHKST03010200",
#     "custtype": "P"
# }
# params = {
#     "FID_ETC_CLS_CODE": "",
#     "FID_COND_MRKT_DIV_CODE": "J",
#     "FID_INPUT_ISCD": "005930",
#     "FID_INPUT_HOUR_1": "093000",
#     "FID_PW_DATA_INCU_YN": "Y"
# }
# try:
#     res = requests.get(url, headers=headers, params=params)
#     data = res.json()
#     print(data["output1"]["hts_kor_isnm"])  # HTS 한글 종목명
#     for item in data["output2"]:
#         print(f"시간: {item['stck_bsop_date']} {item['stck_cntg_hour']} 가격:{item['stck_prpr']}")
# except Exception as e:
#     print(e)
#
# kqi0h06rx-image.png
#
# 출력 결과를 보면 당일 아홉 시 반부터 아홉 시까지의 일분봉 데이터가 잘 도착한 걸 확인할 수 있습니다.
#
# 정리
# 이번 레슨에서는 API 문서를 보면서 리퀘스트를 보내 봤습니다. 처음 써 보시는 거라면, 조금 복잡하게 느껴지실 겁니다. 하지만 어떤 식으로 코딩하는지 큰 흐름은 아셨을 거예요.
#
# API 문서를 읽으면서 리퀘스트에서 보내야 할 값은 무엇인지 파악하고, 파이썬 코드로 옮긴 다음, 받은 리스폰스는 어떤 형태인지 찾아보고 이걸 파이썬으로 활용하는 식이었습니다.
#
# 이 큰 흐름만 잘 이해하셨다면 충분합니다. 이제부터는 API 문서랑 위의 예시 코드를 켜 놓고 여러 번 시도해 보면서 익숙해지는 일만 남았습니다.