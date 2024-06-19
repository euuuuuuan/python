import os
from shutil import copy  # 파일 복사 함수 사용

print(os.listdir('./data'))


for file in os.listdir('./data'):
    file, ext = file.split('.')  # 마침표를 기준으로 확장자 분리
    name, position = file.split('__')  # 언더바를 2개 기준으로 이름과 직무 분리
    src = f'./data/{file}.{ext}'  # 원래 있던 경로
    dest_path = f'./data/{position}'
    if not os.path.exists((dest_path)):
        os.makedirs(dest_path)
    dest = f'./data/{dest_path}/{file}.{ext}' # 이동할 경로
    print(src, '->', dest)

