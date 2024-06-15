# 이번 토픽에서는 파이썬 코드를 써서 네트워크로 한국투자증권에 요청을 보내고, 원하는 데이터를 불러오거나 주식 주문을 넣어 볼 겁니다. 지금은 막막하지만 단계별로 조금씩 알아가다 보면 필요한 만큼은 해낼 수 있을 겁니다. 우선은 먼저 이론적인 것부터 배워 봅시다. 이번 레슨에서는 기본적인 웹 개발 기초 지식을 알아볼게요.
# 
# 에서는 [웹 개발 기초 지식]이라는 토픽에서 웹 개발과 관련된 기본 지식을 배울 수 있어요. 물론 전반적인 내용을 꼼꼼히 알면 좋겠지만, 여기서는 이번 프로젝트를 진행하는 데 꼭 필요한 것들만 간단하게 짚어 보고 넘어가 보겠습니다.
# 
# 일단 자주 쓰는 용어들부터 먼저 알아보고, 리퀘스트와 리스폰스에 대해 자세하게 알아보도록 하겠습니다.
# 
# 서버와 클라이언트
# 우리가 평소에 사용하는 인터넷은 쉽게 얘기하자면 전 세계의 수많은 컴퓨터들이 정보를 서로 교환하는 시스템입니다. 정보를 주고받을 때는 컴퓨터끼리 역할을 나눠서 구분하는데요. 이미 들어 보셨을 수도 있는데, '서버'랑 '클라이언트'로 나눕니다. 주로 정보를 주는 쪽을 서버라고 하고요, 정보가 필요해서 받는 쪽을 클라이언트라고 부르죠. 각각의 역할을 하는 컴퓨터를 서버랑 클라이언트로 구분하기도 하고, 그런 역할을 하는 구체적인 프로그램을 서버랑 클라이언트라고 부르기도 해요.
# 
# 일상생활에서 예를 들자면 네이버 홈페이지를 이용할 때는 네이버에서 서버 역할을 하고, 웹 브라우저가 클라이언트 역할을 하는 거죠. 이번 토픽에서 우리가 만들어 볼 프로그램을 예로 들자면 한국투자증권에서 서버 역할을 하고, 우리가 작성한 프로그램이 클라이언트 역할을 합니다.
# 
# HTTP
# 한국 사람들끼리는 한국말을 쓰고, 중국 사람들끼리는 중국말을 쓰듯이 컴퓨터와 컴퓨터끼리 소통을 하려면 어떤 약속이 필요하겠죠? 인터넷에서는 이런 약속이 바로 HTTP입니다. HTTP라는 약속에 따라서 클라이언트와 서버는 소통을 해요.
# 
# 리퀘스트
# 주로 서버와 클라이언트의 소통은 리퀘스트로부터 시작됩니다. 클라이언트가 서버에 데이터나 서비스를 요청을 하면서 시작하는 건데요. 우리나라 말로는 요청이라고 하고, 영어로는 HTTP 리퀘스트(Request)라고 합니다. 앞으로 우리는 클라이언트가 서버에 뭔가를 요청하는 걸 리퀘스트라고 부르겠습니다.
# 
# 리스폰스
# 요청을 받은 서버는 클라이언트가 원하는 작업을 하고 나서 리스폰스라는 걸로 응답을 해 줍니다. 우리나라 말로는 응답이라고 하고, 영어로는 HTTP 리스폰스(Response)라고 합니다. 앞으로 우리는 서버가 클라이언트에 뭔가를 되돌려 주는 걸 리스폰스라고 부르겠습니다.
# 
# 잠깐 여기까지 배운 걸 다시 한번 정리하고 넘어가 볼까요?
# 
# 서버: 데이터를 제공하는 쪽
# 클라이언트: 데이터를 요청하는 쪽
# HTTP: 인터넷에서 서버와 클라이언트가 소통하는 방식
# 
# 클라이언트가 서버에게 원하는 걸 요청하면(리퀘스트를 보내면) 서버가 클라이언트에게 원하는 걸 보내주는(리스폰스를 보내 주는) 과정으로 소통이 이루어집니다.
# 
# HTTP의 구성 요소
# 이번에는 HTTP의 구성 요소에 대해서 자세히 살펴보도록 하겠습니다.
# 
# 리퀘스트와 리스폰스는 쉽게 말하자면 텍스트로 적혀 있는 메시지에요. 지금 단계에서 당장 이 메시지의 세부적인 내용을 모두 알고 외워야 할 필요는 없고요, 리퀘스트와 리스폰스를 주고받을 때 어떤 방식으로 원하는 정보를 전달할 수 있는지 눈으로 익힌다고 생각하고 살펴봅시다.
# 
# 리퀘스트와 리스폰스를 구체적으로 살펴보기 위해 구글 크롬 브라우저를 열고, 크롬 개발자 도구를 열어 볼게요. 크롬을 켜고 Windows에서는 F12, macOS에서는 Cmd + Option + I를 눌러서 열 수 있습니다. 그럼 이렇게 화면 한쪽에 개발자 도구가 나오거나, 새 창으로 열립니다.
# 
# ci30scp95-image.png
# 
# 그러고 나서 개발자 도구가 열린 상태에서 주소창에다가 learn.it.kr/api/avatars?limit=5&offset=10이라는 주소를 입력하고 접속해 봅시다. 이 주소는  실습 서버에서 사용자들이 생성한 아바타 데이터를 받아오는 주소예요. 여기로 접속하면 웹 브라우저는 실습 서버로 리퀘스트를 보낼 거예요. 그럼 서버는 사용자들이 생성한 아바타 데이터 중 일부를 리스폰스로 보내 줄 겁니다. 이 과정은 주소창에 입력하는 순간 알아서 진행됩니다.
# 
# 리스폰스가 잘 도착하면 아래와 같이 화면에 어떤 데이터가 보일 건데요.
# 
# huvpqrrfz-image.png
# 
# 크롬 브라우저가  실습 서버로 리퀘스트를 보내서 리스폰스로 데이터를 받은 겁니다. 이 상태에서 크롬 개발자 도구의 'Network' 탭으로 들어가 보면 'avatars'라는 이름으로 리퀘스트가 보일 거예요. 이걸 클릭해 보세요.
# 
# 4ftmnv17x-image.png
# 
# 그럼 구체적인 리퀘스트와 리스폰스를 살펴볼 수 있어요.
# 
# rnhlv40p2-image.png
# 
# 주소
# 66wufhwsn-image.png
# 
# 우선 리퀘스트의 주소부터 살펴봅시다.
# 
# 가장 먼저 맨 위에 적혀 있는 https://learn.it.kr/api/avatars?limit=5&offset=10는 클라이언트가 어디로 리퀘스트를 보내는 건지 적은 겁니다.  실습 서버 중에서도 /api/avatars라는 주소로 리퀘스트를 보낸 거예요.
# 
# 여기서 한 가지 특이한 부분이 있어요. ?limit=5&offset=10이라는 부분은 쿼리 문자열, 쿼리 파라미터라고 부르는 부분입니다. 경로에 추가적인 정보를 적어서 전달하는 건데요. 이런 걸 "쿼리 파라미터로 limit 값을 5 그리고 offset 값을 10으로 보낸다"라고 말합니다. 쿼리 파라미터는 하나만 보낼 수 있는 건 아니고 이렇게 여러 개 보낼 수 있어요.
# 
# 메소드
# ybfehd3kd-image.png
# 
# 그리고 리퀘스트 메소드(Request Method)라는 게 있습니다. GET이라는 부분인데요. 쉽게 말해서 클라이언트가 어떤 동작을 하고 싶은지 서버에 간단히 전달하는 동사 같은 건데요. GET 말고도 POST, PATCH 등 다양한 것들이 있습니다. 우리가 이번에 쓸 것만 살펴보자면 클라이언트가 서버로부터 어떤 데이터를 가져올 때는 GET을 쓰고요, 클라이언트가 서버로 어떤 데이터를 보내서 원하는 동작을 할 땐 보통 POST 메소드를 씁니다.
# 
# 헤더
# d0o1roju7-image.png
# 
# 그 아래로 내려 보시면 리스폰스 헤더(Response Headers), 리퀘스트 헤더(Request Headers) 영역이 보입니다. 값이 엄청나게 많죠? 콜론(:) 왼쪽에 적혀 있는 게 헤더 이름이고요, 오른쪽에 적혀 있는 게 각각의 헤더의 값입니다. 헤더는 여러 개를 보낼 수 있습니다. 그리고 리퀘스트뿐만 아니라 리스폰스에서도 헤더를 전달합니다. 스크린샷에서 보시면 서버에서 Content-Type , Date등 다양한 헤더를 보내 주고 있죠?
# 
# 바디
# 클라이언트와 서버가 소통하면서 메소드, 헤더, 쿼리 파라미터로 리퀘스트와 리스폰스를 설명한다면, 구체적인 데이터를 주고받는 건 '바디'라는 걸로 주고받습니다.
# 
# ni8ms9dqi-image.png
# 
# 오른쪽 위에 Response로 들어가 보시면 이런 식으로 데이터가 보이죠? 이런 식으로 서버에서 리스폰스 데이터를 바디에 담아서 보내 주거나, 반대로 클라이언트가 서버에 데이터를 담아서 보내기도 합니다.
# 
# 보통 데이터를 주고받을 때는 받는 쪽에서 받은 데이터의 형식이 어떤 것인지 알 수 있도록 보내는 쪽에서 Content-Type이라는 헤더로 데이터 형식을 알려 줘야 합니다.
# 
# 아까 전에 봤던 스크린샷에서 리스폰스 헤더를 보면 Content-Type: application/json이라고 적혀 있는데요. 이 헤더는 서버가 클라이언트에 데이터를 바디로 보내 주면서, 바디에 있는 데이터의 형식이 application/json이라는 걸 알려 주는 겁니다.
# 
# JSON이란?
# application/json이라는 값에서 특히 주목할 건 바로 json 부분입니다.
# 
# JSON은 HTTP에서 사실상 표준으로 사용하고 있는 데이터 형식인데요. 일반적인 문자열로 데이터를 적어 놓으면, 이걸 컴퓨터가 해석해서 가져다가 쓰는 거예요. 생긴 걸 보시면 파이썬 사전(딕셔너리)랑 닮았죠? 실제로 파이썬에서는 JSON 형식의 데이터를 받으면 보통은 사전 형태로 바꿔서 활용합니다.
# 
# 
# {
#     "count": 40,
#     "next": "https://learn.it.kr/api/avatars/?offset=20&limit=10",
#     "previous": "https://learn.it.kr/api/avatars/?offset=0&limit=10",
#     "results": [
#         {
#             "createdAt": 1713099656000,
#             "updatedAt": 1713099656000,
#             "id": 30,
#             "hairType": "none",
#             "hairColor": "blonde",
#             "skin": "tone200",
#             "clothes": "knitLayered",
#             "accessories": "earbuds"
#         },
#         ...
#         {
#             "createdAt": 1713099656000,
#             "updatedAt": 1713099656000,
#             "id": 21,
#             "hairType": "long1",
#             "hairColor": "blonde",
#             "skin": "tone100",
#             "clothes": "collarBasic",
#             "accessories": "none"
#         }
#     ]
# }
# 정리
# 마지막으로 이번 레슨에서 배운 걸  간단하게 정리하고 넘어갈게요.
# 
# 인터넷에서는 서버와 클라이언트로 역할을 나눠서 컴퓨터(혹은 프로그램)끼리 소통합니다.
# 클라이언트가 데이터를 요청하면, 서버는 데이터를 제공합니다.
# HTTP는 서버랑 클라이언트가 소통하기 위한 약속입니다.
# 클라이언트가 리퀘스트를 보내면 서버는 리스폰스를 보내 줍니다.
# 리퀘스트, 리스폰스에는 다양한 구성 요소들이 있습니다.
# 메소드: GET, POST 등 클라이언트가 어떤 걸 원하는지
# 주소: https://learn.it.kr/api/avatars 같이 리퀘스트를 보낼 서버의 주소
# 쿼리 파라미터: ?limit=5&offset=10처럼 주소 뒤에 붙여서, 옵션처럼 쓸 수 있는 것
# 헤더: Content-Type: application/json처럼 리퀘스트나 리스폰스에서 추가적인 정보를 제공하는 용도
# 바디: 클라이언트가 데이터를 보내거나 서버가 데이터를 보낼 때 바디로 담아서 보냅니다. 주로 사용하는 데이터의 형식은 JSON인데요. 데이터를 보낼 때는 받는 쪽에서 데이터가 어떤 형식인지 알 수 있도록 Content-Type 헤더에 값을 적어서 보내 줘야 합니다. JSON을 사용한다면 Content-Type: application/json을 적어서 보내 주면 됩니다.
# JSON은 서버랑 클라이언트가 데이터를 주고받을 때 자주 사용하는 데이터 형식입니다. 예를 들어서 파이썬에서는 사전 데이터를 JSON 형식으로 바꿔서 보내고, JSON 형식을 서버가 보내 주면 파이썬에서는 사전 데이터로 바꿔서 사용합니다.
# 다음 레슨에서는 파이썬에서 리퀘스트를 보내는 방법과 리스폰스를 받아서 사용하는 방법에 대해 알아볼게요.
# 
