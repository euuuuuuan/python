import os
import time
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# 캐시 설정
response_cache = {}

def get_openai_response(prompt):
    if prompt in response_cache:
        return response_cache[prompt]

    llm = OpenAI(api_key=OPENAI_API_KEY)
    response = llm.generate([prompt])
    response_cache[prompt] = response
    return response

# API 호출 예시
prompt = "Give me a joke"
response = get_openai_response(prompt)

# 결과 출력
print(response)

# DuckDuckGo 검색 도구 사용
search = DuckDuckGoSearchRun()
print(search.run("Obama's first name?"))
print(search.run("이순신 장군이 언제 태어나셨어?"))

# API 호출 사이에 대기 시간 추가 (RateLimit 방지)
time.sleep(1)  # 1초 대기

